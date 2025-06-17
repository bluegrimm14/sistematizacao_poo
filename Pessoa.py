import uuid
from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome: str, email: str):
        self._id = str(uuid.uuid4())
        self._nome = nome
        self._email = email

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def email(self) -> str:
        return self._email