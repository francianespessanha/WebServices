# -*- coding: cp1252 -*-
import datetime


class ComissaoFuncionario:
        def __init__(self, codigoFuncionario, ano, mes):
            self.codigoFuncionario = codigoFuncionario
            self.ano = ano
            self.mes = mes

        def ConsultarVenda(self):
            lista = []
            data = datetime.datetime(2013, 4, 26, 00, 00, 00) 
            lista = [[1,1,1,data,100], [2,2,1,data,900], [3,2,2,data,17]]
           
            return lista            
    
        def CalcularComissao(self):
            valorVenda = 0
            valorComissao=0
            listaVenda = []
            listaVenda = self.ConsultarVenda()
            for item in listaVenda:
                if item[2] == self.codigoFuncionario:
                    if (item[3].year == self.ano) and (item[3].month == self.mes):
                        valorVenda = valorVenda + item[4]
            valorComissao = valorVenda * 0.05

            return valorComissao
                 

