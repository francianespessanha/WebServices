#encoding:utf-8

from SOAPpy import SOAPProxy

srv = SOAPProxy("http://localhost:8087")

codigo = input("Codigo: ")
nome = raw_input("Nome: ")
endereco = raw_input("Endereco: ")
sexo = raw_input("Sexo: ")
datanascimento = raw_input("Data de nascimento: ")

dados = {"codigoFuncinario":codigo, "nome":nome, "endereco":endereco, "sexo":sexo, "datanascimento":datanascimento}

if srv.consultarFuncionario(dados["codigoFuncinario"]):
    print "O usuario com este codigo ja existe!"
else:
    srv.cadastrarFuncionario(dados)
    print "Usuario cadastrado!"
