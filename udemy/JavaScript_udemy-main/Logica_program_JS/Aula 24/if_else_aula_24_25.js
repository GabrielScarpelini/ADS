/*const hora = 30;

if (hora >= 0 && hora <= 11) {
    console.log('Bom dia')
} else if (hora >= 12 && hora <=18){
    console.log('Boa tarde')
} else if (hora >= 19 && hora <= 23){
    console.log('Boa noite')
}else{
    console.log('Seu OS está com a hora errada ow inexistente')
}*/
//continuação Aula 25 

const numero = 10;
if (numero >= 0 && numero <= 5) {
    console.log('Seu número está entre zero e 5 ')
}else{
    console.log('Não está entre 0 e 5')
}

if (numero >= 0 && numero <= 5) {
    console.log('Seu número está entre zero e 5 '); 
} else if (numero >= 6 && numero <=8){
    console.log('Numero está entre 6 e 8'); // o bloco prioriza a primeira verdadeira apenas. 
}else if (numero >= 9 && numero <=11){
    console.log('O número está entre 9 e 11');
}else{
    console.log('O número não está entre 0 e 11');    
}
