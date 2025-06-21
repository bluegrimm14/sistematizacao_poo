from __future__ import annotations #Utilizada para identificr type hints como 
# strings e evitar o ciclo de imports
from Pessoa import Pessoa
from Quarto import Quarto
from Reserva import Reserva
from Hotel import Hotel
from Hospede import Hospede

class Funcionario(Pessoa):
    """Classe que representa um funcionário no sistema de gerenciamentto de hotel.
    
    Attributes:
        _id(str): Identificados único do funcionário, gerado automaticamente com UUID
        _nome(str): Nome completo do funcionário
        _email(str): Endereço de E-mail do funcionário."""
    def __init__(self, nome: str, email: str):
        """Inicializa um objeto funcionário.
        
        Args:
            nome(str): Nome Completo do Funcionário
            email(str): Endereço de E-mail do funcionário"""
        super().__init__(nome, email)

    def __str__(self):
        "Retorna uma representação em String do objeto Funcionário"
        return f"Nome: {self._nome}\nE-mail: {self._email}"
    
    def add_quarto(self,  hotel: Hotel, quarto: Quarto):
        """Método que adiciona um quarto ao Hotel.
        
        Args:
            hotel(Hotel): Hotel referente.
            quarto(Quarto): Quarto a ser adicionado."""
        hotel.add_quarto(quarto)

    def remover_quarto(self, hotel: Hotel, quarto: Quarto):
        """Método que remove um quarto do Hotel.
        
        Args:
            hotel(Hotel): Hotel referente.
            quarto(Quarto): Quarto a ser removido."""
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel: Hotel, hospede: "Hospede"):
        """Método que registra um hóspede no Hotel.
        
        Args:
            hotel(Hotel): Hotel referente.
            hospede(Hospede): Hóspede a ser registrado."""
        hotel.registrar_hospede(hospede)

    def cancelar_reserva(self, hotel: Hotel, reserva: "Reserva"):
        """Método que cancela  uma reserva no Hotel.
        
        Args:
            hotel(Hotel): Hotel referente.
            reserva(Reserva): Reserva a ser cancelada."""
        hotel.cancelar_reserva(reserva)

    def registrar_reserva(self, hotel: Hotel, reserva: "Reserva"):
        """Método que registra uma reserva ao Hotel.
        
        Args:
            hotel(Hotel): Hotel referente.
            reserva(Reserva): Reserva a ser registrada."""
        hotel.add_reserva(reserva)

    def ver_disponibilidade(self, quarto: Quarto):
        """Método que verifica a disponibilidade de um quarto.
        
        Args:
            quarto(Quarto): Quarto referente."""
        print(f"O quarto {quarto.numero} está {quarto.esta_disponivel()}.\n")