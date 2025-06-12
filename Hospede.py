from Pessoa import Pessoa
# from Reserva import Reserva

class Hospede(Pessoa):
    def __init__(self, nome: str, email: str, reservas: list):
        super().__init__(nome, email)
        self._reservas = reservas

        def get_reservas(self):
            return self._reservas  

        def fazer_reserva(self, reserva):
            pass

        def cancelar_reserva(self, reserva):
            pass

        def consultar_reservas(self):
            pass