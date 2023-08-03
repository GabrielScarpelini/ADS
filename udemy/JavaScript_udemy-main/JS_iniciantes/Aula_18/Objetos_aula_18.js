/* só um exemplo de introção a objetos
const array =[1,2,3];
array.push(4);
array[0] = 'gabriel';
//array = 'outra'

console.log(array)

*/

/* aqui é atribuição de pessoas sem objeto
const nome01 = 'Gabriel';
const sobrenome01 = 'Pavia';
const idade01 = 23;
const nome02 = 'Joâo';
const sobrenome = 'Oliveira'
const idade02 = 23;
*/
// criando uma função para criar obejtos 

function criaPessoa (nome, sobrenome, idade) {  // função "factory"
    return {
        nome: nome,                  
        sobrenome: sobrenome,
        idade: idade
// aqui, pode usar somente um nome em 2 pontos EX: nome, sobrenome, idade que o JS já entende
// function criaPessoa (nome, sobrenome, idade) {
//  return {nome, sobrenome, idade};
    };
}
// 
const pessoa1 = criaPessoa('Gabriel', 'Scarpelini', 23);
const pessoa2 = criaPessoa('Rafael' , 'Oliveira', 23);
const pessoa3 = criaPessoa('João', 'Silva', 23);
console.log(pessoa1.nome);
console.log(pessoa2.nome);
console.log(pessoa3.nome);


/*
// aqui é a atribuição de um objeto 
const pessoa1 = {         // definição de obj é similar ao de array porém usa chaves para isso
    nome: 'Gabriel',
    sobrenome: "Pavia",
    idade: 23
}; 

const pessoa2 = {         // definição de obj é similar ao de array porém usa chaves para isso
    nome: 'Julia',
    sobrenome: "Bissoli",
    idade: 28
}; 


console.log(pessoa1.nome);
console.log(pessoa1.sobrenome)
console.log(pessoa2.nome);
console.log(pessoa2.sobrenome)
*/
