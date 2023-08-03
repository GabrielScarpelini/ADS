let umaString = "Um texto de um grande profeta, curte um whiskey bem gelado"
// colocar duas barras invertidas, escapa o caracter da str 
//assim mostrando suas aspas de abertura útil para quando precisa usar duas aspas dentro da string 

// String é indexável 
console.log(umaString[4]);                                 // comando usado para acessar o Índice da lista de carac     
console.log(umaString.charAt(6));                          // aqui outra forma de pegar o ìndice da cadeia de carac  
console.log(umaString.concat(' em um dia'));               // faz a função do concatenar  
console.log(umaString.indexOf('texto', 3));                // mostra onde se inicia a palavra texto, o 3 indica o index minimo pra começar a busca
console.log(umaString.lastIndexOf('o',3));                 // vai buscar de trás pra frente, o 3 é opcional como o de cima
console.log(umaString.match(/[a-z]/g));                    // expressões regulares 
console.log(umaString.search(/[a-z]/));                    // retorna a primeira letra minúscula da str, funciona pelo parâmetro dentro do '[]' 
console.log(umaString.replace(/um/, 'outro'));             // substitui o que tá andes da ',' pra o que tá depois    
console.log(umaString.replace(/t/g, 'b'));                 // troca uma letra por outra, PS o 'g' que  faz trocar todas. 
console.log(umaString.length);                             // pegar o tamanho da string
console.log(umaString.slice(3, 9));                        // ele pega de um valor acima, a um valor abaixo (3, 9) pega o I 4 ao 8 
console.log(umaString.slice(-3));      
console.log(umaString.slice(32));                          // esse exemplo é igual o de cima, o negativo retorna de tras pra frente
console.log(umaString.length - 3);                         // prova real para encontrar o 32 above 
console.log(umaString.substring(umaString.length - 5));    // o substr faz  o mesmo do slice                     
console.log(umaString.split(' ', 3));                      // divide a str (como em python), dps da virgula vai pegar até 3 espaços 
console.log(umaString.toUpperCase());                      // deixa maiúscula as letrar    
console.log(umaString.toLowerCase());                      // deixa minusculas    
                         
