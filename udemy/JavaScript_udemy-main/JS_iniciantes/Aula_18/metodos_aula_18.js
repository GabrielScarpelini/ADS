const pessoa1 = {
    nome: 'Gabriel',
    sobrenome: 'Scarpelini',
    idade: 23, 

    fala () {                 // omitiu a palavra function
        console.log(`A minha idade atual é ${this.idade}`)        // o this está faladno sobre "esse objeto"
    },
    incrementaIdade(){
    this.idade++;           //incrementa de um em um 
    },

}   

pessoa1.fala();
pessoa1.incrementaIdade()
pessoa1.fala()