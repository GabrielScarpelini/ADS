# NOMES DOS ALUNOS (máximo 8 alunos)
# ALUNO 1: Daniel Francelino de Oliveira        RA   2102588
# ALUNO 2: Diego Yann Lima Cardoso de Almeida   RA   2102876
# ALUNO 3: Felipe Singillo de Araujo		    RA   2103062
# ALUNO 4: Gabriel Scarpelini Pavia			    RA   2102341
# ALUNO 5: Gustavo Dias da Silva			    RA	 2102928
# ALUNO 6: Iago Henrique do Prado			    RA	 2102055
# ALUNO 7: Igor de Oliveira Pereira		        RA   2102141
# ALUNO 8: Jean Carlos Gomes de Oliveira		RA   2102935


class Clube:
    def __init__(self):
        self.socios = []

    def associar(self, socio):
        self.socios.append(socio)

    def numero_de_socios(self):
        return (len(self.socios))

    def mes_associacao(self, mes, ano):
        cont = 0
        if mes < 1 or mes > 12:
            raise TypeError
        if len(str(ano)) != 4:
            raise ValueError
        else:
            for x in self.socios:
                if x.mes == mes and x.ano == ano:
                    cont += 1
        return cont

    def expulsar(self, mes, ano):
        lista_expulsos = []
        if mes < 1 or mes > 12:
            raise TypeError
        if len(str(ano)) != 4:
            raise ValueError
        else:
            for x in self.socios:
                if x.mes == mes and x.ano == ano:
                    lista_expulsos.append(x.nome)
            for x in reversed(self.socios):
                if x.nome in lista_expulsos:
                    self.socios.pop(self.socios.index(x))
        lista_expulsos.sort()
        return lista_expulsos


class Socio:
    def __init__(self, nome, cpf, nascimento, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.mes = mes
        self.ano = ano
