from Pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self: str, id, nome: str, email: str, reservas: list): #pendente colocar na futura documentação - list[Reserva]
        super().__init__(id, nome, email)
        self._reservas = reservas

        def fazer_reserva(reserva):
            pass

        def cancelar_reserva(reserva):
            pass

        def consultar_reservas():
            pass