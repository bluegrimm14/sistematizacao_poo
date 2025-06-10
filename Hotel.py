from Quarto import Quarto
from Hospede import Hospede
from Reserva import Reserva


class Hotel:
    def __init__(self):
        self._quartos: list[Quarto] = []
        self._hospedes: list[Hospede] = []
        self._reservas: list[Reserva] = []

    def get_quartos(self):
        return self._quartos
    
    def get_hospedes(self):
        return self._hospedes
    
    def get_reservas(self):
        return self._reservas
    
    def set_reserva(self, reserva: Reserva):
        self._reservas.append[reserva]