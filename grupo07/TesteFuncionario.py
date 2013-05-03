#encoding:utf-8

import unittest
from should_dsl import should
from Funcionario import Funcionario
from ludibrio.mock import Mock

class TesteFuncionario(unittest.TestCase):
    def teste_deletar_funcionario(self):
        with Mock() as vendas:
            vendas.consultarVendasDeFuncionario(1) >> 0
            vendas.consultarVendasDeFuncionario(2) >> 5
        
        func = Funcionario("funcionarios.txt")        
        qtdVendas1 = vendas.consultarVendasDeFuncionario(1)
        qtdVendas2 = vendas.consultarVendasDeFuncionario(2)
        
        func.deletarFuncinario(1,qtdVendas1) |should| equal_to(True)
        func.deletarFuncinario(2,qtdVendas2) |should| equal_to(False)
        
        
