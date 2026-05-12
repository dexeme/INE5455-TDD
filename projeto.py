
class Projeto:
    nome: str

    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("Projeto com nome vazio.")
        self.nome = nome

    def __hash__(self):
        return hash(self.nome)

    def __eq__(self, other):
        return self.nome == other.nome