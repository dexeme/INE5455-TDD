# Alunos: Tiago Faustino de Siqueira e William Kraus

import unittest

from src.ocorrencia import ErroOcorrenciaFechada, EstadoOcorrencia, ErroMembroInvalido
from src.empresa import Empresa, ErroFuncionarioInvalido, ErroFuncionarioRepetido, ErroProjetoInvalido, ErroProjetoRepetido
from src.funcionario import Funcionario
from src.projeto import Projeto, ErroMembroRepetido


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
        self.assertTrue(len(empresa_W.funcionarios) == 1)

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
        self.assertTrue(len(empresa_W.funcionarios) == 2)

    def test_inclui_funcionario_repetido_na_empresa(self):
            empresa_W = Empresa("W")

            william = Funcionario("William Kraus")
            william2 = Funcionario("William Kraus")

            empresa_W.adiciona_funcionario(william)
            with self.assertRaises(ErroFuncionarioRepetido):
                empresa_W.adiciona_funcionario(william2)

            self.assertTrue(len(empresa_W.funcionarios) == 1)

    def test_cria_projeto_valido(self):
        projeto = Projeto("Projeto Legal")
        self.assertTrue(projeto.nome, "Projeto Legal")

    def test_cria_projeto_nome_vazio(self):
        with self.assertRaises(ValueError):
            Projeto("")

    def test_inclui_projeto_na_empresa(self):
        empresa_W = Empresa("W")
        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        self.assertTrue(projeto in empresa_W.projetos)
        self.assertTrue(len(empresa_W.projetos) == 1)

    def test_inclui_projeto_repetido_na_empresa(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        projeto2 = Projeto("Projeto Legal")

        empresa_W.adiciona_projeto(projeto)
        with self.assertRaises(ErroProjetoRepetido):
            empresa_W.adiciona_projeto(projeto2)
        self.assertTrue(len(empresa_W.projetos) == 1)

    def test_inclui_funcionario_em_um_projeto_da_empresa(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        william = Funcionario("William Kraus")
        empresa_W.adiciona_projeto(projeto)
        empresa_W.adiciona_funcionario(william)

        empresa_W.vincula_funcionario(william, projeto)

        self.assertTrue(william in projeto.membros)
        self.assertTrue(len(projeto.membros) == 1)

    def test_inclui_funcionario_repetido_em_um_projeto_da_empresa(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        william = Funcionario("William Kraus")
        william2 = Funcionario("William Kraus")

        empresa_W.adiciona_projeto(projeto)
        empresa_W.adiciona_funcionario(william)

        empresa_W.vincula_funcionario(william, projeto)

        with self.assertRaises(ErroMembroRepetido):
            empresa_W.vincula_funcionario(william2, projeto)
        
        self.assertTrue(william in projeto.membros)
        self.assertTrue(len(projeto.membros) == 1)

    def test_inclui_funcionario_nao_adicionado_a_empresa_em_um_projeto(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        william = Funcionario("William Kraus")
        empresa_W.adiciona_projeto(projeto)

        with self.assertRaises(ErroFuncionarioInvalido):
            empresa_W.vincula_funcionario(william, projeto)
        self.assertTrue(len(projeto.membros) == 0)
        self.assertTrue(william not in projeto.membros)

    def test_inclui_funcionario_em_um_projeto_que_nao_eh_da_empresa(self):
        empresa_W = Empresa("W")

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        
        projeto = Projeto("Projeto Legal")

        with self.assertRaises(ErroProjetoInvalido):
            empresa_W.vincula_funcionario(william, projeto)
        self.assertTrue(len(projeto.membros) == 0)
        self.assertTrue(william not in projeto.membros)

    def test_inclui_ocorrencia_a_projeto(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)

        ocorrencia = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )

        self.assertTrue(ocorrencia in projeto.ocorrencias)
        self.assertTrue(len(projeto.ocorrencias) == 1)

    def test_valida_unicidade_de_chaves_de_ocorrencias(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)

        ocorrencia_1 = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )
        ocorrencia_2 = projeto.cria_ocorrencia(
            resumo="Arruma bug de inserção de ocorrências na empresa.",
            responsavel=william
        )
        ocorrencia_3 = projeto.cria_ocorrencia(
            resumo="Refatora sistema de ocorrências.",
            responsavel=william
        )

        self.assertTrue(ocorrencia_1.chave != ocorrencia_2.chave)
        self.assertTrue(ocorrencia_2.chave != ocorrencia_3.chave)
        self.assertTrue(ocorrencia_1.chave != ocorrencia_3.chave)

    def test_inclui_ocorrencia_a_projeto_com_funcionario_fora_do_projeto(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)

        with self.assertRaises(ErroMembroInvalido):
            projeto.cria_ocorrencia(
                resumo="Implementação do sistema de ocorrências",
                responsavel=william
            )

        self.assertTrue(len(projeto.ocorrencias) == 0)

    def test_ocorrencia_no_estado_aberta_ao_criar(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)
        
        ocorrencia = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )

        self.assertEqual(ocorrencia.estado, EstadoOcorrencia.Aberta)

    def test_ocorrencia_no_estado_fechada_ao_fechar(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)

        ocorrencia = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )

        ocorrencia.fecha()

        self.assertEqual(ocorrencia.estado, EstadoOcorrencia.Fechada)

    def test_muda_responsavel_de_ocorrencia(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)

        tiago = Funcionario("Tiago Siqueira")
        empresa_W.adiciona_funcionario(tiago)
        empresa_W.vincula_funcionario(tiago, projeto)

        ocorrencia = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )

        ocorrencia.muda_responsavel(tiago)

        self.assertEqual(ocorrencia.responsavel, tiago)

    def test_muda_responsavel_de_ocorrencia_para_membro_invalido(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)

        tiago = Funcionario("Tiago Siqueira")
        empresa_W.adiciona_funcionario(tiago)

        ocorrencia = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )

        with self.assertRaises(ErroMembroInvalido):
            ocorrencia.muda_responsavel(tiago)

        self.assertEqual(ocorrencia.responsavel, william)

    def test_muda_responsavel_de_ocorrencia_fechada(self):
        empresa_W = Empresa("W")

        projeto = Projeto("Projeto Legal")
        empresa_W.adiciona_projeto(projeto)

        william = Funcionario("William Kraus")
        empresa_W.adiciona_funcionario(william)
        empresa_W.vincula_funcionario(william, projeto)

        tiago = Funcionario("Tiago Siqueira")
        empresa_W.adiciona_funcionario(tiago)
        empresa_W.vincula_funcionario(tiago, projeto)

        ocorrencia = projeto.cria_ocorrencia(
            resumo="Implementação do sistema de ocorrências",
            responsavel=william
        )

        ocorrencia.fecha()

        with self.assertRaises(ErroOcorrenciaFechada):
            ocorrencia.muda_responsavel(tiago)

        self.assertEqual(ocorrencia.responsavel, william)