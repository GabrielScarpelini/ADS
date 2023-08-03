/** 
 * Aritméticos
 * + Adição e Concatenação 
 * ** Potenciação 
 * % resto da divisão 
 * - / *
 * 
 *  precedencia:
 *      ()
 *      **
 *    / * %  o que aparecer primeiro, left to right  
 *     + - 
 *  Incremento = ++ pré e pós, de 1 em 1
 *  Decremento = -- pré e pós  de 1 em 1
 * 
 * operadores de atribuição 
 *  +=, -=, *=, /=   
 */

let cont = 1;
cont++;         // sinal ++ soma de um em um a uma   variável, pode ser ++var ow var++
let num1 = 'l5'; // o ++antes é bom caso vc queira fazer um log com ele, aí ele altera e muda antes de ler a variável  
const num2 = 10;// -- tira de um a um e é usado como o ++        
console.log(num1 + num2);

console.log(num1 / num2);
console.log(num1 ** num2);
console.log(num1 % num2);
console.log(cont);
console.log(++cont); // pré incremento 


// o JS vai tentar resolver contas com string ex 
console.log(num1 * num2); 

// pra converter uma strig para um numero pode usar number(variável)

const num3 = Number('15') 

console.log(typeof num3, num3) //typeof mostra o tipo da veriável 
