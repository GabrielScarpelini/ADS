/*
Primitivos string, number, boolean, undefined,
null (bigint, symbol)  assim sendo os dados e não o que se atribui a váriaveln são copiados
STRING são imutáveis, ow seja:
nome = 'Gabriel'
nome[0] = "R"
não vai alterar nada 
let a = 5
let b = a       aqui ele copiou o valor, e como é primitivo
                se ele mudar o a o b não muda


-------Dados por Referência (mutável) - array, object, function-------
let a = [1,2,3]  ARRAY
leb b = a     por ser uma passagem por referência caso mude algo no A vai 
              mudar no B tbm, pois indicam para o mesmo lugar na memória  
para copiar e fazer outro valor na memória pode usar:
a = [1,2,3,];
b = [...a];  e é assim que se copia um array 

objeto 

const a - {
    nome:'Luiz',
    sobrenome: 'Pavia'
};
const b = a     aqui é exatamente como array, eles apontam para o mesmo
                lugar na memória se mudar o A muda o B  

para copiar o valor de A para o B em objeto sem referênciar o mesmo lugar na memória

const b = {...a}; e aqui copiou o valor de A 

*/ 