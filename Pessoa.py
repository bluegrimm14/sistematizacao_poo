import uuid
class Pessoa:
    def __init__(self, nome: str, email: str):
        self._id = str(uuid.uuid4())
        self._nome = nome
        self._email = email

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def email(self) -> str:
        return self._email
    
    def __str__(self) -> str:
        return f"Id:{self.id} - Nome:{self.nome} - E-mail:{self.email}"