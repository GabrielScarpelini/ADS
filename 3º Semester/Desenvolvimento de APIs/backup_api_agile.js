/**
 *@NApiVersion 2.1
 *@NScriptType MapReduceScript
 */
 define(['./rsc_api_invoice_batch', 'N/https', 'N/query', 'N/record', 'N/search', 'N/transaction'], function (library, https, query, record, search, transaction) {

    function getInputData() {
        var lista = []
        var page = 1
        var accessAuth = "Bearer 96632cf2ce15b8499a085d0fbff161ccd060187bd2020a72d8f7b8096c6999afa729bd6c7d6e01c09d8c491d5f198212852816bc8b87c08d75e07b8bd590fa72";
        //var accessUrl = "https://api.agilems.com/api/invoices/groups?page="+ page +"&limit=500";
        var accessUrl = "https://api-sandbox.agilems.com/api/invoices/groups?page=" + page + "&limit=500&include=accountReceivable.payment&filter%5Bstatus%5D=in%3APOST,CANCELED&filter%5Bid%5D=10581 ";  // (NÃO APAGAR)--> "https://api-sandbox.agilems.com/api/invoices/groups?page=" + page + "&limit=500&include=accountReceivable.payment&filter%5Bstatus%5D%3Deq=POST&filter%5Bid%5D=9972";
        var accessHeaders = {
            "Content-Type": "application/json",
            Authorization: accessAuth,
            Accept: '*/*'
        };
        var request = https.request({
            method: https.Method.GET,
            url: accessUrl,
            headers: accessHeaders
        });
        var body = JSON.parse(request.body)
        var qtdPages = body.meta.pagination.total_pages + 1
        qtdPages = 1 + 1///////////////////////////////// <===== Apagar
        delete body.meta
        delete body.links
        lista.push(body)
        //log.debug('Body do json', body)
        page += 1
        for (page; page < qtdPages; page++) {
            var accessUrl = "https://api-sandbox.agilems.com/api/invoices/groups?page=" + page + "&limit=500&include=accountReceivable.payment&filter%5Bid%5D=10581 "; // (NÃO APAGAR)--> "https://api-sandbox.agilems.com/api/invoices/groups?page=" + page + "&limit=500&include=accountReceivable.payment&filter%5Bstatus%5D%3Deq=POST&filter%5Bid%5D=9972";
            //log.debug('accessUrl', accessUrl)
            var accessHeaders = {
                "Content-Type": "application/json",
                Authorization: accessAuth,
                Accept: '*/*'
            };
            var request = https.request({
                method: https.Method.GET,
                url: accessUrl,
                headers: accessHeaders
            });
            var body = JSON.parse(request.body)
            delete body.meta
            delete body.links
            lista.push(body)
        }
        return lista
    }

    function map(ctx) {
        try {
            const ListaInvoice = JSON.parse(ctx.value).data
            const ListaIncluded = JSON.parse(ctx.value).included
            const ListaPayments = []
            const ListaReceivable = []
            const ListaCustomer = []
            const ListaNetsuite = []
            const ListaNetsuiteVerificar = [] // Faturas que já existem no Netsuite 
            const ListaInvoiceIds = []

            // Separação das informações adicionais sobre a fatura
            ListaIncluded.forEach(index => {
                if (index.type == 'bankDeposit') {
                    ListaPayments.push(index)
                }
                if (index.type == 'accountReceivable') {
                    ListaReceivable.push(index)
                }
                if (index.type == 'customer') {
                    ListaCustomer.push(index)
                }
            })

            // Busca no Netsuite pelas invoices que já foram criadas (Usando o ID Externo da AgileMS)
            ListaInvoice.forEach(invoice => {
                ListaInvoiceIds.push(invoice.id)
            });
            log.debug('MAP: ListaInvoiceIds', ListaInvoiceIds)
            var queryTxt =
                `select id, custbody_rsc_id_invo_agile
                from transaction
                where recordType = 'invoice' AND custbody_rsc_id_invo_agile in (${ListaInvoiceIds})`

            log.debug('MAP: queryTxt', queryTxt)
            var queryResult = query.runSuiteQL({ query: queryTxt }).asMappedResults();
            log.debug('MAP: queryResult', queryResult)

            queryResult.forEach(invoiceNetsuite => { // <-------------------
                ListaNetsuite.push(invoiceNetsuite.custbody_rsc_id_invo_agile)
            });
            log.debug('MAP: ListaNetsuite', ListaNetsuite)

            // Filtro para comprar se as faturas já existem no Netsuite e incluí-las nas respectívas listas
            const NovasInvoices = ListaInvoice.filter(function (invoice) {
                if (!ListaNetsuite.includes(invoice.id)) {
                    return true
                } else {
                    ListaNetsuiteVerificar.push(invoice)
                }
            });
            log.debug('MAP: NovasInvoices', NovasInvoices)
            log.audit('MAP: Resultado de comparação de invoices: ', { invoicesApi: ListaInvoiceIds.length, invoicesNetsuite: ListaNetsuite.length, NovasInvoices: NovasInvoices.length, ListaNetsuiteVerificar: ListaNetsuiteVerificar.length })

            ctx.write({
                key: 'listasMap',
                value: {
                    ListaNetsuiteVerificar: ListaNetsuiteVerificar,
                    NovasInvoices: NovasInvoices,
                    ListaReceivable: ListaReceivable,
                    ListaPayments: ListaPayments,
                    ListaCustomer: ListaCustomer,
                }
            })

        } catch (e) {
            log.error('MAP: Erro global: ', e)
        }
    }

    function reduce(ctx) {
        try {
            const FaturasExistentes = JSON.parse(ctx.values).ListaNetsuiteVerificar
            const NovasInvoices = JSON.parse(ctx.values).NovasInvoices
            const ListaReceivable = JSON.parse(ctx.values).ListaReceivable
            const ListaPayments = JSON.parse(ctx.values).ListaPayments
            const ListaCustomer = JSON.parse(ctx.values).ListaCustomer
            const InvoicesCriadas = []
            const InvoicesAnuladas = []
            const PagamentosCriados = []
            const PagamentosAnulados = []
            log.debug('Reduce Params', { FaturasExistentes: FaturasExistentes, NovasInvoices: NovasInvoices, ListaReceivable: ListaReceivable, ListaPayments: ListaPayments, ListaCustomer: ListaCustomer })
            log.audit('Reduce Params Quantity', { FaturasExistentes: FaturasExistentes.length, NovasInvoices: NovasInvoices.length, ListaReceivable: ListaReceivable.length, ListaPayments: ListaPayments.length, ListaCustomer: ListaCustomer.length })


            // criando novas faturas e seus pagamentos

            NovasInvoices.forEach(invoice => {
                try {
                    var statusFatura = invoice['attributes'].status
                    if (statusFatura == 'CANCELED') {
                        throw `Não é possível criar a fatura:${invoice.id} no Netsuite porque ela está cancelada!`
                    }
                    if (invoice.relationships.accountReceivable.data.length != 0) { // Fatura é parcelada
                        // Padronizar o item sempre como mensalidade
                        // verificar se existe pagamento parcial
                        library.createInstallmentInvoice(PagamentosCriados, InvoicesCriadas, ListaReceivable, ListaCustomer, invoice)
                    }

                } catch (e) {
                    log.error(`Não é possível criar a fatura:${invoice.id}`, e)
                }
            })

            // criando os pagamentos de faturas já existentes no netsuite

            // A busca irá retornar várias faturas com o mesmo Id da Agile, pois quando uma fatura tem 3 parcelas, são criadas 3 faturas no netsuite
            FaturasExistentes.forEach(invoice => {
                try {
                    var queryTxt =
                    `select id, custbody_rsc_id_invo_agile, custbody_rsc_id_inst_agile, foreigntotal, foreignamountunpaid
                    from transaction
                    where recordType = 'invoice' AND custbody_rsc_id_invo_agile = ${invoice.id}`
                    const ParcelasInvoiceNetsuite = query.runSuiteQL({ query: queryTxt }).asMappedResults();

                    ParcelasInvoiceNetsuite.forEach(parcela => {
                        library.verificarAnulamento(InvoicesAnuladas, PagamentosAnulados, invoice, parcela.id)
                        library.verificarPagamento(parcela, ListaReceivable, invoice.id, PagamentosCriados)

                    })
                } catch (e) {
                    log.error(`Não é possível criar a fatura:${invoice.id}`, e)
                }
            })

            log.debug('Invoices criadas: ', InvoicesCriadas)
            log.audit('Total de invoices e pagamentos criados', { invoices: InvoicesCriadas.length, pagamentos: PagamentosCriados.length })
            log.audit('Total de invoices e pagamentos Anulados', { invoices: InvoicesAnuladas.length, pagamentos: PagamentosAnulados.length })
        } catch (e) {
            log.error(`Erro global Reduce:`, e)
        }


    }

    function summarize(summary) {

    }

    return {
        getInputData: getInputData,
        map: map,
        reduce: reduce,
        summarize: summarize
    }
});
