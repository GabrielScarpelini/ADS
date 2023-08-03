function funcao(vetor, x){
    let i = 0
    for (i = 0; i < vetor.length && vetor[i] != x; i = i + 1){}
    if (i < vetor.length){
        console.log(vetor[i])
        console.log(i)
        return true
    }else{
        return false
    }
}    
let pessoas = ['ana', 'beatriz', 'carlos', 'daniel','eduardo']
let a = funcao(pessoas, 'ana')
let b = funcao(pessoas, 'joão')
let c = funcao(pessoas, 'eduardo')
let d = funcao(pessoas, 'fabiana')

console.log(a)
console.log(b)
console.log(c)
console.log(d)


