# Alunos: Tiago Faustino de Siqueira e William Kraus

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.ocorrencia import Ocorrencia


class ErroFuncionarioSobrecarregado(Exception):
    pass

class Funcionario:
    nome: str
    ocorrencias_abertas: list["Ocorrencia"]

    def __init__(self, nome: str):
        if not nome:
            raise ValueError("Funcionario com nome vazio.")
        self.nome = nome
        self.ocorrencias_abertas = []

    def __eq__(self, other):
        return self.nome == other.nome