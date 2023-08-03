//array é bem parecido com listas em python
// pode usar lista.length pra descobrir o tamanho da lista
let lista = ['Luiz', 'Maria', 'João']

lista.push("Rafael")                     // adiciona no final da lista
lista[lista.length] = 'Gabriel'          // adiciona no fim da lista
lista.unshift('Luiza')                   // adiciona no índice zero 
const last = lista.pop()                 // remove o valor do último índice, pode ser atribuido a uma variável pra salvar o valor deletado
const first = lista.shift()              // remove o primeiro índice da lista
delete lista[1]                          // deleta o valor do índice, porém não deleta o índice em si (1 empty item)

console.log(typeof lista);               // ele vai retornar um objeto pois o array é um objeto
console.log(lista instanceof Array)      // retorna um boolean sobre a lista ser um Array

console.log(lista.slice(0, -1))          // trabalha como um range 0, 2 vai pegar o índice 0 e 1 apenas omitindo o 2 
console.log(lista.length)
console.log(lista)
console.log(last)                        // printando o que foi removido da lista 
console.log(first)                       // printando o que foi removido da lista 


// JavaScript tem um Valor Padrao para tudo que não existe, sendo ele Undefined 