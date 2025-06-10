class Pessoa:
    def __init__(self, id: str, nome: str, email: str):
        self._id = id
        self._nome = nome
        self._email = email

    def get_id(self) -> str:
        return self._id
    
    def get_nome(self) -> str:
        return self._nome
    
    def get_email(self) -> str:
        return self._email