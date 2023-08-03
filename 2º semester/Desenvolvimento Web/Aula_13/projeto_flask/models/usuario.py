class Aluno: 
	# Classe que representa dados simplificados de alunos
	def __init__(self, usuario, senha, nome, curso, data_inicio, notas):
		self.usuario = usuario
		self.senha = senha
		self.nome = nome
		self.curso = curso
		self.data_inicio = data_inicio
		self.notas = notas

class BancoDeDados:
	# Classe que simula operações sobre um banco de dados
	def __init__(self):
		# cria um "banco de dados" artificial
		self.__bd = [
			Aluno('gabriel', '1234', 'Gabriel Scarpelini', 'Ciência da Computação', '01/02/2021', [6.5, 6.0, 9.8]),
			Aluno('igor', '1111', 'Igor Pereira', 'Análise de Sistemas', '13/08/2020', [10.0, 5.5, 8.9]),
			Aluno('lago', '9876', 'Iago Henrique', 'Redes de Computadores', '20/06/2021', [7.5, 7.8, 9.5]),
			Aluno('daniel', '5678', 'Daniel Francelino', 'Administração', '15/01/2019', [6.3, 8.8, 7.2])
		]
	
	def existe_aluno(self, usuario, senha):
		# checa se um aluno existe pelo seu usuário e senha
		for aluno in self.__bd:
			if aluno.usuario == usuario and aluno.senha == senha:
				return True
		return False
	
	def obter_dados(self, usuario):
		# obtém dados de um aluno através do seu usuário, se esse existir
		for aluno in self.__bd:
			if aluno.usuario == usuario:
				return aluno
		return None