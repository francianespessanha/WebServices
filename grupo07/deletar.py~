#encoding:utf-8

from SOAPpy import SOAPProxy

srv = SOAPProxy("http://localhost:8087")
vendas = SOAPProxy("")

codigo = input("Codigo: ")

qtdVendas = vendas.consultarVendasDeFuncionario(codigo)

if srv.deletarFuncinario(codigo,qtdVendas):
    srv.deletarFuncinario(codigo,qtdVendas)
    print "Funcionario deletado."
else:
    print "Funcionario possui vendas e nao pode ser deletado."
