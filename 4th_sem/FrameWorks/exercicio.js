fetch()

const express = require('express')

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

fetch("")
  .then(function (response) {
    return response.blob();
  })

console.log(lista)

