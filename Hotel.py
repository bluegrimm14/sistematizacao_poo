from Quarto import Quarto
from Hospede import Hospede
from Reserva import Reserva

class Hotel:
    """Classe que representa o hotel no sistema de gerenciamento de hotel.
    
    Attributes:
        _quartos(list[Quarto]): Lista de quartos no Hotel.
        _hospedes(list[Hospede]): Lista de hóspedes no Hotel.
        _reservas(list[Reserva]): Lista de reservas no Hotel."""
    def __init__(self):
        """Método que inicializa o objeto Hotel."""
        self._quartos: list[Quarto] = []
        self._hospedes: list[Hospede] = []
        self._reservas: list[Reserva] = []

    @property
    def quartos(self) -> list[Quarto]:
        """Getter do atributo _quartos -> 
        list[Quarto]: self._quartos"""
        return self._quartos
    
    @property
    def hospedes(self) -> list[Hospede]:
        """Getter do atributo _hospedes -> 
        list[Hospede]: self._hospedes"""
        return self._hospedes
    
    @property
    def reservas(self) -> list[Reserva]:
        """Getter do atributo _reservas -> 
        list[Reserva]: self._reservas"""
        return self._reservas
    
    def add_reserva(self, reserva: Reserva):
        """Método que adiciona uma reserva ao Hotel.
        
        Args:
            reserva(Reserva): Reserva a ser adicionada."""
        reserva.quarto.reservar()
        self._reservas.append(reserva)
        print("Reserva adicionada com Sucesso.")

    def  add_quarto(self, quarto: Quarto):
        """Método que adiciona um quarto ao Hotel.
        
        Args:
            quarto(Quarto): Quarto a ser adicionado."""
        self._quartos.append(quarto)
        print(f"O Quarto {quarto.numero} foi adicionado com Sucesso.")

    def remover_quarto(self, quarto: Quarto):
        """Método que remove um quarto do Hotel.
        
        Args:
            quarto(Quarto): Quarto a ser removido."""
        if quarto in self._quartos:
            self.quartos.remove(quarto)
            print("Quarto Removido com Sucesso.")
        else:
            print("Este quarto não existe no Hotel.")

    def registrar_hospede(self, hospede: Hospede):
        """Método que registra um hospede no Hotel.
        
        Args:
            hospede(Hospede): Hóspede a ser registrado."""
        self._hospedes.append(hospede)
        print(f"O(A) Hóspede {hospede.nome} foi Registrado com Sucesso.")

    def cancelar_reserva(self, reserva: Reserva):
        """Método que cancela uma reserva no Hotel. Ao cancelar uma reserva, está é excluida da lista de reservas do hotel, o quarto da reserva fica disponível e o hóspede dessa reserva é excluido da lista de hóspedes.
        
        Args:
            reserva(Reserva): Reserva a ser cancelada."""
        if reserva in self._reservas:
            reserva.quarto.liberar()
            self._hospedes.remove(reserva.hospede)
            self._reservas.remove(reserva)
            print(f"Reserva, e Respectivo Hóspede, Removidos com Sucesso.")
        else:
            print("Esta reserva não existe no Hotel.")