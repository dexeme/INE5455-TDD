class Empresa():
    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("Empresa com nome vazio.")
        self.nome = nome