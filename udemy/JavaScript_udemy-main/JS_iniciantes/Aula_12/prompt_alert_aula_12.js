alert(`Com nossa mensagem.`)

// o log é um metodos que esta dentro do objeto console 

alert('Olá mundo')
console.log('Olá');
confirm('Confirma que deseja dormir?')
const confirma = confirm('Relamente deseja apagar?');
alert(confirma);

let num1 = Number(window.prompt(`Digite um número:`));
let num2 = Number(window.prompt(`Digite outro valor:`));

const show = confirm('Deseja que ocorra a operação?');

 // se não for usar o valor da soma pode ser como o alert abaixo, se não soma numa variavel e exibe ela no alert
if (show == true)                           
    alert(`A resposta é ${num1 + num2}`);   // if criado por teste meu
                                            // working properly 
else 
    alert('você negou a operação...');
