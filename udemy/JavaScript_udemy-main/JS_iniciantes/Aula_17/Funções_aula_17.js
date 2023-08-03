function saudacao(nome) {    //define a função
    console.log(`Bom dia ${nome}`);
    return 123456
}
function soma(x, y){            // aqui se for passado str como parâmetro ele irá concatenar, o ideal seria incluir uma condicional
    const resultado = x + y;    // para evitar que isso acontecesse 
    return resultado
}

function multiplica(x = 5, y = 5){     // aqui foi passado os valores padrôes para os paraêmetros 
    const multi = x * y
    return multi 
}

const multi = multiplica(5)         // como foi definido os valores padrôes, se passar um parâm apenas irá funcionar normal. 
 
console.log(soma(3, 2));
console.log(soma(3, 1));
console.log(multiplica(10));

let nome = 'Mike'
saudacao(nome); 
const vari = saudacao(nome)


// a definição de funções são bem parecidas com python 

// criação de função anônima, é obrigatòrio o uso do ponto e virgula no final. 

const raiz = function (n) {
    return n ** 0.5; // 
};//

console.log(raiz(9))
console.log(raiz(16))
console.log(raiz(25))

// criação da arrow function 

const root = n => n ** 0.5; // a seta faz o papel da function na anônima e caso, não é obg a usar ponto e virgula
                            // e caso tenha só um param pode elliminar os parenteses 
console.log(root(9))
console.log(root(16))
console.log(root(25))