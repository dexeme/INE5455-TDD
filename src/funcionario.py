# Alunos: Tiago Faustino de Siqueira e William Kraus

class Funcionario:
    nome: str

    def __init__(self, nome: str):
        if not nome:
            raise ValueError("Funcionario com nome vazio.")
        self.nome = nome

    def __eq__(self, other):
        return self.nome == other.nome