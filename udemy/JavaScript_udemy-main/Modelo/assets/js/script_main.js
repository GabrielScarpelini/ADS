function meuEscopo(){    
    const form = document.getElementById("formulario")
    const resultado = document.getElementById("resultado")   // puxando a div de detro do form para voltar o valor das operações para dentro do HTML
    
    function Indice(evento){
        evento.preventDefault();

        let peso = document.getElementById("peso");          //pega o valor do campo do formulário. peso 
        let altura = document.getElementById("altura")       //pega o valor do campo do form. altura    
        
        peso = Number(peso.value)
        altura = Number(altura.value)                        // atribui os valores as variáveis, e já as converte 

        function imc(peso, altura){                          // função que calcula o IMC
                result = peso / (altura/100)**2
            return result
        }
        const massa = imc(peso, altura)                      // atribui o resultado da função a uma variável    
        
        
        if (peso <= 0 || altura <= 0){                     
            resultado.innerHTML = `<p id="Red" > Valor inválido</p>`
        }else if (massa < 18.5){                                    //condicional com a variável criada acima
            resultado.innerHTML = `<p id="green" > Seu IMC é ${massa.toFixed(2)} (Abaixo do peso)`  // retorna o valor para dentro do HTML 
        }else if (massa > 18.5 && massa < 24.9){
            resultado.innerHTML = `<p id="green" > Seu IMC é ${massa.toFixed(2)} (Peso normal)`     // retorna o valor para dentro do HTML
        }else if (massa > 25 && massa < 29.9){
            resultado.innerHTML = `<p id="green" > Seu IMC é ${massa.toFixed(2)} (Sobrepeso)`      // retorna o valor para dentro do HTML
        }else if (massa > 30 && massa < 34.9){
            resultado.innerHTML = `<p id="green" > Seu IMC é ${massa.toFixed(2)} (Obesidade grau 1)` // retorna o valor para dentro do HTML    
        }else if (massa > 35 && massa < 39.9){
            resultado.innerHTML = `<p id="Green" > Seu IMC é ${massa.toFixed(2)} (Obesidade grau 2)` // retorna o valor para dentro do HTML    
        }else if (massa > 40){
            resultado.innerHTML = `<p id="green" > Seu IMC é ${massa.toFixed(2)} (Obesidade grau 3)` // retorna o valor para dentro do HTML    
        }else if(peso !== Number || altura !== Number){
            resultado.innerHTML = `<p id="Red" > Valor inválido</p>`                                 // retorna o valor para dentro do HTML
        }
        
        }
        form.addEventListener('submit', Indice)

}





meuEscopo()