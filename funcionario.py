
class Funcionario:
    nome: str

    def __init__(self, nome: str):
        if not nome:
            raise ValueError("Funcionario com nome vazio.")
        self.nome = nome