from __future__ import annotations
from Hospede import Hospede
from Quarto import Quarto

class Reserva:
    def __init__(self, hospede: "Hospede", quarto: Quarto):
        self._hospede = hospede
        self._quarto = quarto

    # def __str__(self):
    #     return f"Hospede: {self._hospede} \nQuarto: {self._quarto}"

    @property
    def hospede(self) -> "Hospede":
        return self._hospede
    
    @property
    def quarto(self) -> Quarto:
        return self._quarto