from Quarto import Quarto
from Hospede import Hospede
from Reserva import Reserva

class Hotel:
    def __init__(self):
        self._quartos: list[Quarto] = []
        self._hospedes: list[Hospede] = []
        self._reservas: list[Reserva] = []

    @property
    def quartos(self) -> list[Quarto]:
        return self._quartos
    
    @property
    def hospedes(self) -> list[Hospede]:
        return self._hospedes
    
    @property
    def reservas(self) -> list[Reserva]:
        return self._reservas
    
    @reservas.setter
    def reservas(self, reserva: Reserva):
        self._reservas.append[reserva]

    def  add_quarto(self, quarto: Quarto):
        self._quartos.append(quarto)
        print("Quarto adicionado com Sucesso!")

    def remover_quarto(self, quarto: Quarto):
        if quarto in self._quartos:
            self.quartos.remove(quarto)

    def registrar_hospede(self, hospede: Hospede):
        self._hospedes.append(hospede)

    def cancelar_reserva(self, reserva: Reserva):
        if reserva in self._reservas:
            self._reservas.remove(reserva)