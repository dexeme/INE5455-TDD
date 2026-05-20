from enum import Enum

from src.funcionario import ErroFuncionarioSobrecarregado, Funcionario

class EstadoOcorrencia(Enum):
    Aberta = 0
    Fechada = 1

class TipoOcorrencia(Enum):
    Tarefa = 0
    Bug = 1
    Refatoracao = 2


class PrioridadeOcorrencia(Enum):
    Baixa = 0
    Media = 1
    Alta = 2


class ErroMembroInvalido(Exception):
    pass

class ErroOcorrenciaFechada(Exception):
    pass

class Ocorrencia:
    chave: int
    tipo: TipoOcorrencia
    resumo: str
    responsavel: Funcionario
    estado: EstadoOcorrencia
    prioridade: PrioridadeOcorrencia
    
    def __init__(self, projeto, chave: int, tipo: TipoOcorrencia, resumo: str):
        self._projeto = projeto
        self.chave = chave
        self.resumo = resumo
        self.estado = EstadoOcorrencia.Aberta
        self.tipo = tipo
        self.responsavel = None
    
    def __eq__(self, other):
        return self.chave == other.chave
    
    def fecha(self):
        self.estado = EstadoOcorrencia.Fechada

        if self in self.responsavel.ocorrencias_abertas:
            self.responsavel.ocorrencias_abertas.remove(self)

    def muda_responsavel(self, responsavel: Funcionario):
        if responsavel not in self._projeto.membros:
            raise ErroMembroInvalido(f"{responsavel.nome} não está na lista de membros do projeto {self._projeto.nome}.")
        if self.estado == EstadoOcorrencia.Fechada:
            raise ErroOcorrenciaFechada(f"A ocorrência {self.chave} está fechada.")
        
        if len(responsavel.ocorrencias_abertas) >= 10:
            raise ErroFuncionarioSobrecarregado(f"{responsavel.nome} já é responsável por 10 ocorrências abertas.")
        
        
        if self.responsavel and self in self.responsavel.ocorrencias_abertas:
            self.responsavel.ocorrencias_abertas.remove(self)
        
        if self not in responsavel.ocorrencias_abertas:
            responsavel.ocorrencias_abertas.append(self)

        self.responsavel = responsavel
    
    def muda_prioridade(self, prioridade: PrioridadeOcorrencia):
        if self.estado == EstadoOcorrencia.Fechada:
            raise ErroOcorrenciaFechada(f"A ocorrência {self.chave} está fechada.")
        self.prioridade = prioridade
