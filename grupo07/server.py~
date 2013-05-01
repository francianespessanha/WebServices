#encoding:utf-8

from SOAPpy import SOAPServer
from Funcionario import Funcionario

func = Funcionario("funcionarios.txt")

srv = SOAPServer(("localhost",8087))
srv.registerFunction(func.cadastrarFuncionario)
srv.registerFunction(func.consultarFuncionario)
srv.registerFunction(func.deletarFuncinario)
srv.serve_forever()
