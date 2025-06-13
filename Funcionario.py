from __future__ import annotations #Utilizada para identificr type hints como 
# strings e evitar o ciclo de imports
from Pessoa import Pessoa
from Quarto import Quarto
from Reserva import Reserva
from Hotel import Hotel
from Hospede import Hospede

class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)
    
    def add_quarto(self,  hotel: Hotel, quarto: Quarto):
        hotel.add_quarto(quarto)

    def remover_quarto(self, hotel: Hotel, quarto: Quarto):
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel: Hotel, hospede: "Hospede"):
        hotel.registrar_hospede(hospede)

    def cancelar_reserva(self, hotel: Hotel, reserva: "Reserva"):
        hotel.cancelar_reserva(reserva)

    def registrar_reserva(self, hotel: Hotel, reserva: "Reserva"):
        hotel.add_reserva(reserva)