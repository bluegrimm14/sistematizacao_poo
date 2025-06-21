import uuid
from abc import ABC, abstractmethod
class Pessoa(ABC):
    """Classe Abstrata base que representa uma pessoa no sistema de gerenciameento de hotel. Como não pode ser instanciada, serve como classe mãe para outras classes do projeto.
    
    Attributes:
        _id(str): Identificados único da pessoa, gerado automaticamente com UUID
        _nome(str): Nome completo da Pessoa
        _email(str): Endereço de E-mail da pessoa.
    """
    def __init__(self, nome: str, email: str):
        """Inicializa  nova instância de pessoa. 
        
        Args:
            _nome(str): Nome completo da Pessoa
            _email(str): Endereço de E-mail da pessoa.
        """
        self._id = str(uuid.uuid4())
        self._nome = nome
        self._email = email

    @abstractmethod
    def __str__(self) -> str:
        """Retorna uma representação em String do Objeto"""
        pass

    @property
    def id(self) -> str:
        """Getter do atributo _id ->
        str: self._id"""
        return self._id
    
    @property
    def nome(self) -> str:
        """Getter do atributo _nome ->
        str: self._nome"""
        return self._nome
    
    @property
    def email(self) -> str:
        """Getter do atributo _email ->
        str: self._email"""
        return self._email