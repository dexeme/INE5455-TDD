# Alunos: Tiago Faustino de Siqueira e William Kraus

import unittest

class TestesTDD(unittest.TestCase):

    def test_cria_empresa(self):
        empresa_W = Empresa("W")
        self.assertEqual(empresa_W.nome, "W")

if __name__ == "__main__":
    unittest.main()
