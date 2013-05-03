#!/usr/bin/env python
#-*- encoding: iso-8859-1 -*-

from SOAPpy import SOAPServer
from produto import Produto


def cadastrarProduto(descricao, preco, codigoFornecedor):
    produto1 = Produto()
    return produto1.cadastrarProduto(descricao, preco, codigoFornecedor)


def deletarProduto(codigoProduto):
    produto2 = Produto()
    return produto2.deletarProduto(codigoProduto)


serv = SOAPServer(("localhost", 8080))
serv.registerFunction(cadastrarProduto)
serv.registerFunction(deletarProduto)

serv.serve_forever()

