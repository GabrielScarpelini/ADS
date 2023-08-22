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



function criaP () {                               
    const p = document.createElement('p');          //createElement usado pra criar algo no document 
    return p;
}
function setResultado (msg, isValid) {
    const resultado = document.querySelector('#resultado');
    resultado.innerHTML = '';
    
    const p = criaP();
  
    if (isValid) {
        p.classList.add('paragrafo-resultado');        // p criado na função cria p, e aqui atribui uma classe a ele 
    } else {
        p.classList.add('bad');
    }
  
    p.innerHTML = msg;
    resultado.appendChild(p);
}
  
const form = document.querySelector("#formulario")
console.log(document)

form.addEventListener("submit", async (e) => {
    e.preventDefault()
    const aluno =  e.target.querySelector("#studant")
    console.log(aluno.checked)
    
    var tipo;
    const name =  e.target.querySelector("#name")
    const email =  e.target.querySelector("#email")
    const cpf_cnpj =  e.target.querySelector("#cnpf")
    const birthday =  e.target.querySelector("#bday")
    const phone =  e.target.querySelector("#tel")
    const txt = `Olá ${name.value}, Seu cadastro foi finalizado, favor verifique
    seu email (${email.value}) para finalizar o seu cadastro, CPF/CNPJ ${cpf_cnpj.value},
    data de nascimento ${birthday.value}, Tel ${phone.value}`
    
    if(aluno.checked == true){
        alert("é aluno")
    }else{
        alert("é professor")
    }

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

    // chamar o post pelo fetch
    // const response = await fetch("https://api-go-wash-efc9c9582687.herokuapp.com/api/user-teste", init)
    // const dados = await response.json()
    // console.log(dados)

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