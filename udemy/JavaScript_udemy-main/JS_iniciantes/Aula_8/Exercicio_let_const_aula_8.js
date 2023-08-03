/**
 * Luiz otávio miranda, tem 30 anos, pesa 84 kg 
 * tbm 1.8 de altura e seu IMC É DE 25.925952952
 * Luiz Otávio nasceu em 1980
 */
const nome = 'Luiz Otávio';
const sobrenome = 'Miranda';
const idade = 30;
const peso = 84
const alturaEmM = 1.8;
let imc; // peso / (altura * altura)
let anoNascimento; 
// string em template 
console.log(`${nome} ${sobrenome}, tem ${idade} anos, pesa ${peso}kg   
tem ${alturaEmM.toFixed(2)} de altura e seu IMC é de ${imc = peso / (alturaEmM * alturaEmM)}
${nome} nasceu em ${anoNascimento = 2022 - idade}.`)

console.log(imc)
console.log(alturaEmM)