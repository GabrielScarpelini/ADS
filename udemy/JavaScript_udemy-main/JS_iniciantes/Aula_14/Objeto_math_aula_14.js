let num1 = 9 
let num2 = Math.floor(num1);                                 //arredondando para o num int abaixo
let num2 = Math.ceil(num1);                                  //arredondando para o num int acima
let num2 = Math.round(num1);                                 //arredonda para o número int mais próximo ex 9.49 vai pra 9 e 9.50 vai para 10
console.log(Math.max(1,2,3,4,-50,-1000,15000,9,8,7,6))       //mostra o maior valor de uma lista 
console.log(Math.min(1,2,3,4,-50,-1000,15000,9,8,7,6))       //mostra o menor valor de uma lista 
console.log(Math.random());                                  //pega valores randomicos entre 0 e 1 
const aleatorio = Math.random() * (10 - 5) + 5               //usando variaveis pra pegar valor random, pegando o intervalo entre 10 e 5 
const aleatorio = Math.round(Math.random() * (10 - 5) + 5);  //mesmo exemplo acima, porém o colocando como valor int  
console.log(Math.PI);                                        //pegando o pi pelo math
console.log(Math.pow(2,10));                                 //potencias, sendo 2 elevado a 10 
console.log(2**10);                                          //mostrando o exemplo acima com operadores
console.log(Math.PI);                                        //chamando pi pela função math 
console.log(num1 ** (1/2)) ow 0.5                            //forma matemática de fazer raiz quadrada 
 //aqui no JS pode dividir por 0 que dá o resultado de infinity
