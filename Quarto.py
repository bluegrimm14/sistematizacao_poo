class Quarto:
    """Classe que representa um quarto no sistema de gerenciamento de hotel.
    
    Attributes:
        _numero(int): Número do quarto.
        _tipo(str): Tipo do quarto.
        _disponivel(bool): Disponibilidade do Quarto. True == Disponível e False == Indisponível."""
    def __init__(self, numero: int, tipo: str, disponivel: bool):
        """Método que inicializa o objeto Quarto..
        
        Args:
            numero(int): Número Inteiro do Quarto
            tipo(str): Tipo do Quarto
            disponivel(bool): DIsponibilidade do Quarto. True == Disponível e False == Indisponível."""
        self._numero = numero
        self._tipo = tipo
        self._disponivel = disponivel

    def __str__(self) -> str:
        """Representação em String do objeto Quarto."""
        return f"Número: {self._numero}\nTipo: {self._tipo}\nDisponibilidade: {self._disponivel}"
    
    def __repr__(self):
        """Representação oficial, normalmente em coleções do python, do objeto Quarto."""
        return f"Número: {self._numero} - Tipo: {self._tipo} - Disponibilidade: {self._disponivel}"

    @property
    def numero(self) -> int:
        """Getter do atributo _numero ->
        int: self._numero."""
        return self._numero
    
    @property
    def tipo(self) -> str:
        """Getter do atributo _tipo ->
        str: self._tipo."""
        return self._tipo
    
    @property
    def disponivel(self) -> bool:
        """Getter do atributo _disponivel ->
        bool: self._disponivel."""
        return self._disponivel
    
    def reservar(self):
        """Método que reserva o quarto, tornando este indisponível."""
        self._disponivel = False

    def liberar(self):
        """Método que libera o quarto, tornando este disponível."""
        self._disponivel = True 

    def esta_disponivel(self) -> str:
        """Método que consulta a disponibilidade do quarto."""
        if self._disponivel == True:
            return "Disponível"
        else:
            return "Indisponível"
    