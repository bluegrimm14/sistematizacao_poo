from __future__ import annotations
from Hospede import Hospede
from Quarto import Quarto

class Reserva:
    """Classe que representa uma reserva no sistema de gerenciamento de hotel.
    
    Attributes:
        _hospede(Hospede): Hospede desta reserva.
        _quarto(Quarto): Quarto hospedado da reserva."""
    def __init__(self, hospede: "Hospede", quarto: Quarto):
        """Método que inicializa o objeto Reserva.
        
        Args:
            hospede(Hospede): Hospede da reserva.
            quarto(Quarto): Quarto hospedado da reserva."""
        self._hospede = hospede
        self._quarto = self.valida_quarto(quarto)

    def __str__(self):
        """Representação em String do objeto Reserva."""
        return f"Hospede: {self._hospede.nome}\nQuarto: {self._quarto.numero}"
    
    def __repr__(self):
        """Representação oficial, normalmente em coleções do python, do objeto Reserva."""
        return f"Hospede: {self._hospede.nome} - Quarto: {self._quarto.numero}"

    @staticmethod
    def valida_quarto(quarto: Quarto):
        if quarto.disponivel == True:
            return quarto
        else:
            raise ValueError ("Este Quarto se Encontra Indisponível!")

    @property
    def hospede(self) -> "Hospede":
        """Getter do atributo _hospede -> 
        Hospede: self._hospede."""
        return self._hospede
    
    @property
    def quarto(self) -> Quarto:
        """Getter do atributo _quarto -> 
        Quarto: self._quarto."""
        return self._quarto