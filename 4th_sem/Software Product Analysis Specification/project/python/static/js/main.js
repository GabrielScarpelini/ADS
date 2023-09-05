// const mysql = require('/mysql2')

// const conn = mysql.createConnection({
//     host: "localhost",
//     user: "teste",
//     password: "teste1",
//     database: "teste fullstack"
// })

// conn.connect(function(error){
//     if (error){
//         alert("erro ao conectar com o Mysql")
//     }else{
//         alert("rodando")
//     }
// })



function TestaCPF(strCPF) {
    var Soma;
    var Resto;
    Soma = 0;
  if (strCPF == "00000000000") return false;

  for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
  Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11))  Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10)) ) return false;

  Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11))  Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11) ) ) return false;
    return true;
}
  
const form = document.querySelector("#formulario")
console.log(document)
window.alert("esta com JS")

form.addEventListener("submit", async (e) => {
    e.preventDefault()
    const aluno =  e.target.querySelector("#studant")
    console.log(aluno.checked)
    
    var tipo;
    const name = e.target.querySelector("#name")
    const email = e.target.querySelector("#email")
    const cpf_cnpj = e.target.querySelector("#cpf")



    const txt = `Olá ${name.value}, Seu cadastro foi finalizado, favor verifique
    seu email (${email.value}) para finalizar o seu cadastro, CPF/CNPJ ${cpf_cnpj.value},
    data de nascimento ${birthday.value}, Tel ${phone.value}`


    console.log(txt)

    setResultado(txt, true)
    // setTimeout(() => {window.location.reload()},5000)

    aluno.checked == true ? tipo = "1" : tipo = "2"


    const jsonPost = {
        "name": name.value,
        "email": email.value,
        "user_type_id": tipo,
        "password":123456,
        "is_active": "1",
        "cpf_cnpj": cpf_cnpj.value,
        "terms": "1",
        "birthday": birthday.value,
        "phone": phone.value
    }

    //no init foram passados todos os params que precisamos para usar o fetch no método post
    
    console.log(jsonPost)
    const init = {
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify(jsonPost)   
    }

})

// {
//     "name": "Gabriel",
//     "email": "gabriel.spavia@gmail.com",
//     "user_type_id": "1",
//     "password": "123456",
//     "is_active": "1",
//     "cpf_cnpj": "51804500000117",
//     "terms": "1",
//     "birthday": "17/09/1998",
//     "phone": "48999999999"    
//   }  