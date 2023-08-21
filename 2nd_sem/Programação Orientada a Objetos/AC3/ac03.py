# NOMES DOS ALUNOS (máximo 8 alunos)
# ALUNO 1: Daniel Francelino de Oliveira        RA   2102588
# ALUNO 2: Diego Yann Lima Cardoso de Almeida   RA   2102876
# ALUNO 3: Felipe Singillo de Araujo    	    RA   2103062
# ALUNO 4: Gabriel Scarpelini Pavia			    RA   2102341
# ALUNO 5: Gustavo Dias da Silva			    RA	 2102928
# ALUNO 6: Iago Henrique do Prado			    RA	 2102055
# ALUNO 7: Igor de Oliveira Pereira		        RA   2102141
# ALUNO 8: Jean Carlos Gomes de Oliveira		RA   2102935


class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, tipo):
        super().__init__(nome, nascimento)
        self.tipo = tipo
        self.casa = None
        self.disciplinas = []
        self.__triunfos = 0
        self.__mau_feitos = 0

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos += quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos += quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos


class Professor(Pessoa):
    def __init__(self, nome, nascimento):
        super().__init__(nome, nascimento)
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.__diretor = None
        self.__monitor = None

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_diretor(self):
        return self.__diretor

    def get_monitor(self):
        return self.__monitor


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Torneio:
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def marcar_ponto(self, casa, quantidade):
        if casa.nome == self.casa1.nome:
            self.__pontos_casa1 += quantidade
        else:
            self.__pontos_casa2 += quantidade

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2
