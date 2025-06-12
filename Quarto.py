class Quarto:
    def __init__(self, numero: int, tipo: str, disponivel: bool):
        self._numero = numero
        self._tipo = tipo
        self._disponivel = disponivel

    @property
    def numero(self):
        return self._numero
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def disponivel(self):
        return self._disponivel
    
    def reservar():
        pass

    def liberar():
        pass

    def esta_disponivel():
        pass
    