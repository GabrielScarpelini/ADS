from flask import Flask, render_template, request, session, redirect # aqui são os imports necessários
from models.usuario import BancoDeDados #importação do banco de dados que deve estar no mesmo nível desse arquivo na pasta flask
from datetime import timedelta # esse import explicarei mais pra frete

app = Flask(__name__)
app.secret_key = '&eeiji43#@7763@@%¨$#@niunfw!@&%' # esse é o "cookie" o q faz o usuário já logado entrar direto sem o login em caso de fechar a aba

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1, seconds=30)
# essa função acima permite que o cookie perda a validade após 1:30min, pois assim não dará pra
# para usar um cookie antigo para invadir o perfil de alguém

@app.route('/login', methods=['GET','POST']) # criando o path da tela login, com os dois metodos get e post
def login():
    msg_erro = ''
    if request.method == 'POST':     # verificando se vc vai enviar o form 
        usuario = request.form.get('usuario') # pegando dados do html                        #request.args é para o get
        senha = request.form.get('senha')     # pegando dados do html  
        bd = BancoDeDados()                   #iniciando o banco de dados 
        if bd.existe_aluno(usuario, senha):   # chamando um metodo que verifica se existe alino  
            session['usuario'] = usuario      # se sim usa dicionário para pegar os valores 
            return redirect('/area_logada')   # o redirect envia para outra pagina
        else:
            msg_erro = 'Usuário e/ou senha inválidos' # se o usuário não existir no bd aparecerá essa msg
    return  render_template('login.html', erro=msg_erro) # e voltará para tela de login

@app.route('/area_logada') #criou a areá logada (lembrando que tem html pra isso)
def area_logada():
    if 'usuario' in session: # se for o usuário que está na sessão (o cookie válido)
        bd = BancoDeDados() # pega o bd novamente 
        dados_aluno = bd.obter_dados(session['usuario']) # atribuiu o dados_alunos ao metodo da classe obter_dados
        # dados_alunos agora é um objeto e pode acessar os valores 
        
        return render_template('area_logada.html', aluno=dados_aluno) #agora aluno será um obj epuxará informações pelo html
    else:
        return redirect('/login')# se o cookie não estiver válido, retornará sempre para pg de login

# esse bloco abaixo é bem semelhante ao de cima, só lembrando que para pegar atributos como EX nome
# vc precisará fazer isso no html, colocando aluno.nome onde vc quer que ele apareça
@app.route('/notas') 
def notas():
    if 'usuario' in session: 
        bd = BancoDeDados()  
        dados_aluno = bd.obter_dados(session['usuario'])  
        return render_template('notas.html', aluno=dados_aluno)
    else:
        return redirect('/login')
        

@app.route('/logout') # aqui criada a tela de logout
def sair():
    session.clear() # limpando o cookie da sessão, assim o usuário será deslogado
    return redirect('/login') # e será redirecionado para tela de login novamente
app.run(debug=True)