from src.emailServico import EmailServico

class EmailServicoDummy(EmailServico):

    def enviar_email(self, mensagem: str):
        raise NotImplemented('Método não implementado!')