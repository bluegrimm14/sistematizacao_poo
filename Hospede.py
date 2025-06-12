from Pessoa import Pessoa
from Reserva import Reserva
from __future__ import annotations
class Hospede(Pessoa):
    def __init__(self, nome: str, email: str, reservas: list["Reserva"]):
        super().__init__(nome, email)
        self._reservas = reservas

    @property
    def reservas(self) -> list["Reserva"]:
        return self._reservas  

    def fazer_reserva(self, reserva: "Reserva"):
        pass

    def cancelar_reserva(self, reserva: "Reserva"):
        pass

    def consultar_reservas(self):
        pass