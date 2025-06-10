from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id: str, nome: str, email: str):
        super().__init__(id, nome, email)
    
    def add_quarto(self,  hotel, quarto):
        pass

    def remover_quarto(hotel, quarto):
        pass

    def registrar_hospede(hotel, hospede):
        pass

    def cancelar_reserva(hotel, reserva):
        pass