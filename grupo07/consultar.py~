#encoding:utf-8

from SOAPpy import SOAPProxy

srv = SOAPProxy("http://localhost:8087")

codigo = input("Codigo: ")

if srv.consultarFuncionario(codigo):
    print srv.consultarFuncionario(codigo)
else:
    print "Funcionario com este codigo nao existe"
