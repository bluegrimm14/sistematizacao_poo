from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)
    
    def add_quarto(self,  hotel, quarto):
        pass

    def remover_quarto(self, hotel, quarto):
        pass

    def registrar_hospede(self, hotel, hospede):
        pass

    def cancelar_reserva(self, hotel, reserva):
        pass