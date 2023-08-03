//IEEE 754 2008 padrao para os floats não ficarem 100% precisos 


let num1 = 0.7;    //number
let num2 = 0.1;      //number 

num1 += num2    //esperado 0.8 real 0.79999999
num1 += num2    //esperado 0.9 real 0.89999999 
num1 += num2    // esperado 1 real 0.9999999 

num1 = Number(num1.toFixed(2))         // pra corrigir o problema acima usar essa estrutura
console.log(num1);
console.log(Number.isInteger(num1));

//console.log(num1.toString() + num2);     // trasnformou pra concatenar o num p str
//num1 = num1.toString()                   // transformou definitivo p str  

// console.log(typeof num1);

//console.log(num1.toString(2));            // aqui está fazendo uma represantação binária do num1 definido pelo valor dentro do()

//console.log(num1.toFixed(2));             // pra definir as casa decimais definido pelo valor dentro do ()
                                            // BP fazer contas com o número original, e quando for exibir colocar o .toFixed

//console.log(Number.isInteger(num1));      // verificando se o número é inteiro 

//let temp = num1 * 'Olá';                    // tentando multiplicar str por number, aparece NaN not a number
//console.log(Number.isNaN(temp));            // perguntando ao JS se é uma conta inválida da op da variável temp

