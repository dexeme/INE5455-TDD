# Alunos: Tiago Faustino de Siqueira e William Kraus

import unittest

from empresa import Empresa
from funcionario import Funcionario

class TestesTDD(unittest.TestCase):

    def test_cria_empresa(self):
        empresa_W = Empresa("W")
        self.assertEqual(empresa_W.nome, "W")

    def test_cria_empresa_nome_vazio(self):
        with self.assertRaises(ValueError):
            Empresa("")

    def test_inclui_funcionario_na_empresa(self):
        empresa_W = Empresa("W")

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)

        self.assertTrue(william in empresa_W.funcionarios)


if __name__ == "__main__":
    unittest.main()
