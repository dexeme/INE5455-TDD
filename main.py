# Alunos: Tiago Faustino de Siqueira e William Kraus

import unittest

from empresa import Empresa, ErroFuncionarioRepetido
from funcionario import Funcionario
from projeto import Projeto


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

    def test_cria_funcionario_nome_vazio(self):
        with self.assertRaises(ValueError):
            Funcionario("")

    def test_inclui_dois_funcionarios_na_empresa(self):
        empresa_W = Empresa("W")

        william = Funcionario("William Kraus")
        tiago = Funcionario("Tiago Siqueira")

        empresa_W.adiciona_funcionario(william)
        empresa_W.adiciona_funcionario(tiago)

        self.assertTrue(william in empresa_W.funcionarios)
        self.assertTrue(tiago in empresa_W.funcionarios)

    def test_inclui_funcionario_repetido_na_empresa(self):
            empresa_W = Empresa("W")

            william = Funcionario("William Kraus")
            william2 = Funcionario("William Kraus")

            empresa_W.adiciona_funcionario(william)
            with self.assertRaises(ErroFuncionarioRepetido):
                empresa_W.adiciona_funcionario(william2)

    def test_cria_projeto_valido(self):
        projeto = Projeto("Projeto Legal")
        self.assertTrue(projeto.nome, "Projeto Legal")

    def test_cria_projeto_nome_vazio(self):
        with self.assertRaises(ValueError):
            Projeto("")

if __name__ == "__main__":
    unittest.main()
