from funcionario import Funcionario
from projeto import Projeto


class Empresa():
    funcionarios: list[Funcionario]
    projetos: list[Projeto]

    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("Empresa com nome vazio.")
        self.nome = nome

        self.funcionarios = []
        self.projetos = []

    def adiciona_funcionario(self, funcionario: Funcionario):
        if funcionario in self.funcionarios:
            raise ErroFuncionarioRepetido(f"{funcionario.nome} já está na lista de funcionários da empresa {self.nome}.")
        self.funcionarios.append(funcionario)

    def adiciona_projeto(self, projeto: Projeto):
        if projeto in self.projetos:
            raise ErroProjetoRepetido(f"{projeto.nome} já está na lista de projetos da empresa {self.nome}.")
        self.projetos.append(projeto)

class ErroFuncionarioRepetido(Exception):
    pass

class ErroProjetoRepetido(Exception):
    pass