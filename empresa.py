from funcionario import Funcionario

class Empresa():
    funcionarios: list[Funcionario]

    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("Empresa com nome vazio.")
        self.nome = nome

        self.funcionarios = []

    def adiciona_funcionario(self, funcionario: Funcionario):
        if funcionario in self.funcionarios:
            raise ErroFuncionarioRepetido(f"{funcionario.nome} já está na lista de funcionários da empresa {self.nome}.")
        self.funcionarios.append(funcionario)


class ErroFuncionarioRepetido(Exception):
    pass