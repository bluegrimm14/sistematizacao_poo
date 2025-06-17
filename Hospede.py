from __future__ import annotations
from Pessoa import Pessoa
# from Reserva import Reserva
class Hospede(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)
        self._reservas: list = []

    def __str__(self):
        return f"Nome: {self._nome}\nE-mail: {self._email}\nQtd. Reservas: \
        {len(self._reservas)}"

    @property
    def reservas(self) -> list:
        return self._reservas  

    def fazer_reserva(self, reserva ):
        self._reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self.reservas.remove(reserva)

    def consultar_reservas(self) -> list:
        return self._reservas