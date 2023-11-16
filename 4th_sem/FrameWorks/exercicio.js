fetch("https://api-go-wash-efc9c9582687.herokuapp.com/api/dados", {
method: 'GET',
}).then(response => response.json()
).then(result => console.log(JSON.stringify(result.data)))


// fetch("http://api-go-wash-efc9c9582687.herokuapp.com/api/",{
//     method: "POST",
//     body: JSON.stringify({
//         nome:"Test"
//     }),
//     headers: 'Content-Type: application/json',
//     mode: "cors",
// }).then(response =>{
//     return response
// }).then(response =>{
//     console.log(response)
// })

// var myHeaders = new Headers();

// var myInit = {
//   method: "POST",
//   "Authoriazation"
//   mode: "cors",
//   cache: "default",
// };



var lista = [{
    nome: "coca cola",
    qnt: 5,
    valor: 20
},
{
    nome: "sprite",
    qnt: 4,
    valor: 15
},
{
    nome: "pepsi",
    qnt: 3,
    valor: 10
}]

for(var i = 0; i<lista.length;i++){
    lista[i].valor_total = lista[i].qnt * lista[i].valor
}

console.log(lista)

