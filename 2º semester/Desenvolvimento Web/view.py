from random import randint


class ParImpar():
    def __init__(self, numero, escolha):
        self.numero_jogador = numero
        self.numero_maquina = randint(1, 10)
        self.escolha_jogador = escolha
        self.resultado_par = False

    def calculo(self):
        print(f"A máquina escolheu o número: {self.numero_maquina}")
        self.total = self.numero_jogador + self.numero_maquina
        print(f"{self.numero_jogador} + {self.numero_maquina}",
              (f" = {self.numero_jogador + self.numero_maquina}"))
        if self.total % 2 == 0:
            self.resultado_par = True
            print(f"{self.total} é par.")
        else:
            self.resultado_par = False
            print(f"{self.total} é impar.")
        self.vencedor()

    def vencedor(self):
        if self.escolha_jogador == "par" and self.resultado_par:
            print("Parabéns você venceu!")
        elif self.escolha_jogador == "impar" and not self.resultado_par:
            print("Parabéns, você venceu!")
        else:
            print("Você perdeu!")


numero = int(input("Qual número deseja colocar:  "))
escolha = input("Par ou Impar?")


jogo1 = ParImpar(numero, escolha)
jogo1.calculo()