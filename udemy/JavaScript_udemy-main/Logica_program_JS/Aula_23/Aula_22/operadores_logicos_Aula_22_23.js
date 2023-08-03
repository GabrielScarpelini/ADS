/*
Operadores lógicos 
&&  AND 
||  OR
!   NOT 


// Avaliação de curto circuito
ex:
console.log("Luiz" && "Maria")

/ se algo aqui estiver errado, a avaliação retorna
o que estiver errado


valores que sempre retornarão falso por sí só
FALSY    
*false 
 0 
'' "" `` 
null / undefined 
NaN

diferente deles, esss valores retornam true 

ex 
function falaOi() {
    return 'Oi';
}

const vaiExecutar = "joãozinho"         aqui ele vai dar true por conta que 
console.log(vaiExecutar && falaOi());   joaozinho n é uma str vazia 


function falaOi() {
    return 'Oi';
}

const vaiExecutar = ""                aqui vai dar false pela str vazia  
console.log(vaiExecutar && falaOi());

PARA O || OR 
 no ex: (0 || false || null || 'Gabriel Scarpelini' || true)

 ele vai retornar na tela o primeiro valor true 


*/