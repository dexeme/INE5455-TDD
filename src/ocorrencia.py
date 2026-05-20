from enum import Enum

from src.funcionario import Funcionario

class EstadoOcorrencia(Enum):
    Aberta = 0
    Fechada = 1

class ErroMembroInvalido(Exception):
    pass

class Ocorrencia:
    chave: int
    resumo: str
    responsavel: Funcionario
    estado: EstadoOcorrencia
    
    def __init__(self, projeto, chave: int, resumo: str):
        self._projeto = projeto
        self.chave = chave
        self.resumo = resumo
        self.estado = EstadoOcorrencia.Aberta
    
    def __eq__(self, other):
        return self.chave == other.chave
    
    def fecha(self):
        self.estado = EstadoOcorrencia.Fechada

    def muda_responsavel(self, responsavel: Funcionario):
        if responsavel not in self._projeto.membros:
            raise ErroMembroInvalido(f"{responsavel.nome} não está na lista de membros do projeto {self._projeto.nome}.")
        self.responsavel = responsavel
