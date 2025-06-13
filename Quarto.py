class Quarto:
    def __init__(self, numero: int, tipo: str, disponivel: bool):
        self._numero = numero
        self._tipo = tipo
        self._disponivel = disponivel

    def __str__(self) -> str:
        return f"{self._numero} - {self._tipo} - {self._disponivel}"

    @property
    def numero(self) -> int:
        return self._numero
    
    @property
    def tipo(self) -> str:
        return self._tipo
    
    @property
    def disponivel(self) -> bool:
        return self._disponivel
    
    def reservar(self):
        self._disponivel = False

    def liberar(self):
        self._disponivel = True 

    def esta_disponivel(self) -> str:
        if self._disponivel == True:
            return "Disponível"
        else:
            return "Indisponível"
    