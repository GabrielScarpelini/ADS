from abc import ABCMeta, abstractmethod

class EmailServico(metaclass=ABCMeta):
    @abstractmethod
    def enviar_email(self, mensagem: str):
        pass