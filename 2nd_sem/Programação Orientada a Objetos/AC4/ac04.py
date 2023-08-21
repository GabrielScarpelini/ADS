from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, cpf, rg, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.data_nascimento = data_nascimento

    @abstractmethod
    def get_rg(self):
        pass

    @abstractmethod
    def get_cpf(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, cpf, rg, data_nascimento, codigo_matricula,
                 data_matricula, endereco, telefone, altura, peso):
        super().__init__(nome, cpf, rg, data_nascimento)
        self.codigo_matricula = codigo_matricula
        self.data_matricula = data_matricula
        self.__endereco = endereco
        self.__telefone = telefone
        self.altura = altura
        self.peso = peso
        self.faltas = 0

    def conta_falta(self, falta):
        self.faltas += falta

    def mostra_faltas(self):
        print(f'{self.nome} tem {self.faltas} faltas')

    def get_rg(self):
        return Pessoa.get_rg(self)

    def get_cpf(self):
        return Pessoa.get_cpf(self)

    def get_endereco(self):
        print(f'Endereço do aluno é {self.__endereco}')

    def get_telefone(self):
        print(f'Telefone do aluno é {self.__telefone}')


class Turma:
    def __init__(self, horario_aula, tempo_duracao, data_inicial,
                 data_final, tipo_atv, professor, monitor):
        self.alunos = []
        self.horario_aula = horario_aula
        self.tempo_duracao = tempo_duracao
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.tipo_atv = tipo_atv
        self.professor = professor
        self.monitor = monitor

    def mostra_turma(self):
        for aluno in self.alunos:
            print(f'Alunos {aluno.nome}')

        print(f'Horario da aula {self.horario_aula}')
        print(f'Tempo de duração {self.tempo_duracao}')
        print(f'Data de Início {self.data_inicial}')
        print(f'Data prevista de Término {self.data_final}')
        print(f'Tipo de Atividade {self.tipo_atv.nome}')
        print(f'Professor dessa atividade {self.professor.nome}')
        print(f'Monitor dessa atividade {self.monitor.nome}')

    def insere_aluno(self, aluno):
        print(f'O aluno {aluno.nome} está sendo inserido')
        self.alunos.append(aluno)

    def remove_aluno(self, aluno):
        if len(self.alunos) == 0:
            print('Não há alunos para ramover')
        else:
            print(f'Removendo {aluno.nome}')
            for x in range(len(self.alunos)-1):
                if self.alunos[x].nome == aluno:
                    self.alunos.pop(x)


class Instrutor(Pessoa):
    def __init__(self, cpf, rg, nome, data_nascimento,
                 especialidade, telefone):
        super().__init__(nome, cpf, rg, data_nascimento)
        self.especialidade = especialidade
        self.telefone = telefone
        self.turmas = []

    def get_cpf(self):
        return Pessoa.get_cpf(self)

    def get_rg(self):
        return Pessoa.get_rg(self)


class Atividade:
    def __init__(self, nome):
        self.nome = nome,
        self.professores = []

    def insere_prof(self, nome):
        print(f'Professor {nome} está na lista de intrutores dessa atividade')
        self.professores.append(nome)

    def remove_prof(self, nome):
        if len(self.professores) == 0:
            print('Não há professores para essa atividade')
        elif nome in self.professores:
            print(f'Professor {nome} está sendo removido...')
            for x in self.professores:
                if x == nome:
                    self.professores.pop(x)
        else:
            print('Professor não encontrado')

atividade1 = Atividade("Natação")
atividade2 = Atividade("Muay Thai")
atividade3 = Atividade("Jiu Jitsu")

aluno1 = Aluno('Lago', 12345678910, 12345678, '11/11/1995', 11111,
               '24/12/2020', 'Frando da Rocha', 912345678, 1.78, 68)
aluno2 = Aluno('Daniel', 11111111111, 11111111, '24/12/1999', 22222,
               '21/03/2021', 'SP', 912345999, 2.00, 65)
aluno3 = Aluno('Igor', 22222222222, 22222222, '12/03/2002', 33333,
               '22/06/2021', 'Jandira', 999968379, 1.89, 56)
aluno4 = Aluno('Gabriel', 33333333333, 33333333, '17/09/1998', 44444,
               '22/10/2020', 'SBC', 966929048, 1.79, 93)

instrutor1 = Instrutor(44444444444, 44444444, 'Paulo',
                       '12/12/1990', 'Muay Thai', 989789789)
instrutor2 = Instrutor(55555555555, 55555555, 'Rafael',
                       '29/02/1964', 'Natação', 987654321)
instrutor3 = Instrutor(66666666666, 66666666, 'Gustavo',
                       '20/04/1989', 'Jiu Jitsu', 964441234)
instrutor4 = Instrutor(45612345678, 252525252, 'Gabriel',
                       '17/09/1998', 'dormir', 96969696969)


turma1 = Turma('11:30am', '1h30', '12/05/2022', '12/05/2023', atividade1,
               instrutor2, aluno1)
turma2 = Turma('1:15pm', '1h00', '28/02/2022', '28/03/2023', atividade2,
               instrutor1, aluno1)
turma3 = Turma('12:35pm', '1h30', '01/02/2021', '06/09/2022', atividade3,
               instrutor3, aluno1)

aluno1.conta_falta(2)
aluno1.mostra_faltas()
aluno1.get_rg()
aluno1.get_cpf()
aluno1.get_endereco()
aluno1.get_telefone()

instrutor1.get_rg()
instrutor1.get_cpf()

turma1.insere_aluno(aluno1)
turma1.insere_aluno(aluno2)
turma1.insere_aluno(aluno3)
turma1.remove_aluno(aluno2)
turma1.mostra_turma()
