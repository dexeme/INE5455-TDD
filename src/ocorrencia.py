from enum import Enum

from src.funcionario import Funcionario

class EstadoOcorrencia(Enum):
    Aberta = 0
    Fechada = 1

class Ocorrencia:
    chave: int
    resumo: str
    responsavel: Funcionario
    estado: EstadoOcorrencia
    
    def __init__(self, chave: int, resumo: str):
        self.chave = chave
        self.resumo = resumo
        self.estado = EstadoOcorrencia.Aberta
    
    def __eq__(self, other):
        return self.chave == other.chave
    
    def fecha(self):
        self.estado = EstadoOcorrencia.Fechada

