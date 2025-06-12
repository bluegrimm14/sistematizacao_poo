from Quarto import Quarto
from Hospede import Hospede
from Reserva import Reserva


class Hotel:
    def __init__(self):
        self._quartos: list[Quarto] = []
        self._hospedes: list[Hospede] = []
        self._reservas: list[Reserva] = []

    @property
    def quartos(self):
        return self._quartos
    
    @property
    def hospedes(self):
        return self._hospedes
    
    @property
    def reservas(self):
        return self._reservas
    
    @property
    def reserva(self, reserva: Reserva):
        self._reservas.append[reserva]