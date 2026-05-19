# Alunos: Tiago Faustino de Siqueira e William Kraus

from src.funcionario import Funcionario


class Projeto:
    nome: str
    membros: list

    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("Projeto com nome vazio.")
        self.nome = nome
        self.membros = []

    def vincula_funcionario(self, funcionario: Funcionario):
        if funcionario in self.membros:
            raise ErroMembroRepetido(f"{funcionario.nome} já está na lista de membros do projeto {self.nome}.")
        self.membros.append(funcionario)

    def __hash__(self):
        return hash(self.nome)

    def __eq__(self, other):
        return self.nome == other.nome

class ErroMembroRepetido(Exception):
    pass
