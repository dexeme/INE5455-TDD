# Alunos: Tiago Faustino de Siqueira e William Kraus

from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia, PrioridadeOcorrencia, TipoOcorrencia


class Projeto:
    nome: str
    membros: list
    ocorrencias: list[Ocorrencia]
    proxima_chave_de_ocorrencia: int

    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("Projeto com nome vazio.")
        self.nome = nome
        self.membros = []
        self.ocorrencias = []
        self.proxima_chave_de_ocorrencia = 0

    def vincula_funcionario(self, funcionario: Funcionario):
        if funcionario in self.membros:
            raise ErroMembroRepetido(f"{funcionario.nome} já está na lista de membros do projeto {self.nome}.")
        self.membros.append(funcionario)

    def cria_ocorrencia(
        self,
        tipo: TipoOcorrencia,
        resumo: str,
        responsavel: Funcionario,
        prioridade: PrioridadeOcorrencia = PrioridadeOcorrencia.Media
    ):
        chave = self.proxima_chave_de_ocorrencia
        self.proxima_chave_de_ocorrencia += 1

        ocorrencia = Ocorrencia(self, chave, tipo, resumo)
        ocorrencia.muda_responsavel(responsavel)
        ocorrencia.muda_prioridade(prioridade)
        self.ocorrencias.append(ocorrencia)

        return ocorrencia

    def __eq__(self, other):
        return self.nome == other.nome

class ErroMembroRepetido(Exception):
    pass
