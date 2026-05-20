
from src.funcionario import Funcionario


class Ocorrencia:
    chave: int
    resumo: str
    responsavel: Funcionario
    
    def __init__(self, chave: int, resumo: str):
        self.chave = chave
        self.resumo = resumo
    
    def __eq__(self, other):
        return self.chave == other.chave
