from __future__ import annotations
from Pessoa import Pessoa
# from Reserva import Reserva
class Hospede(Pessoa):
    """Classe que representa um hóspede no sistema de gerenciamento de hotel.
    
    Attributes:
        _id(str): Identificados único do hóspede, gerado automaticamente com UUID
        _nome(str): Nome completo do hóspede.
        _email(str): Endereço de E-mail do hóspede.
        _reserva(list): Lista das Reservas do Hóspede"""
    def __init__(self, nome: str, email: str):
        """Método que inicializa o objeto Hospede.
        
        Args:
            nome(str): Nome Completo do Hóspede.
            email(str): Endereço de E-mail do Hóspede."""
        super().__init__(nome, email)
        self._reservas: list = []

    def __str__(self):
        """Representação em String do objeto Hóspede"""
        return f"Nome: {self._nome}\nE-mail: {self._email}\nQtd. Reservas: \
        {len(self._reservas)}"

    @property
    def reservas(self) -> list:
        """Getter do atributo _reservas -> 
        list: self._reserva"""
        return self._reservas  

    def fazer_reserva(self, reserva ):
        """Método que faz uma reserva no hotel.
        
        Args:
            reserva(Reserva): Reserva a ser efetuada."""
        self._reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        """Método que cancela uma reserva no Hotel.
        
        Args:
            reserva(Reserva): Reserva a ser cancelada"""
        self.reservas.remove(reserva)

    # def consultar_reservas(self) -> list:
    #     """Método que consulta as reservas do Hóspede."""
    #     return self._reservas