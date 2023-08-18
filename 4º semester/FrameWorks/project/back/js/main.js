
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

form.addEventListener("submit", (e) => {
    e.preventDefault()
    const aluno =  e.target.querySelector("#studant")
    console.log(aluno.checked)
    
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

    setResultado(txt, true)
    // setTimeout(() => {window.location.reload()},5000)
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