from Hospede import Hospede
from Quarto import Quarto

class Reserva:
    def __init__(self, hospede: Hospede, quarto: Quarto):
        self._hospede = hospede
        self._quarto = quarto

    @property
    def hospede(self):
        return self._hospede
    
    @property
    def quarto(self):
        return self._quarto