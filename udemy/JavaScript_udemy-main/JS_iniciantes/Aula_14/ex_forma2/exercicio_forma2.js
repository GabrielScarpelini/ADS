const num = Number(prompt('Digite um número'));
const num_titulo = document.getElementById('jake');
const div = document.getElementById('bloo');

num_titulo.innerHTML= num;
div.innerHTML = `<p>Raiz quadrada: ${(num **0.5).toFixed(2)} </p> 
                 <p> ${num} é inteiro: ${Number.isInteger(num)}</p> 
                 <p> É NaN: ${Number.isNaN(num)}</p> 
                 <p> Arredondando para baixo: ${Math.floor(num)} </p> 
                 <p> Arredondando para cima: ${Math.ceil(num)} </p> 
                 <p> Com duas casas decimais: ${num.toFixed(2)}`