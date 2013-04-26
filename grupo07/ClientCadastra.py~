#encoding:utf-8

from SOAPpy import SOAPProxy

servico = SOAPProxy("hhtp://localhost:8080")

codigo = raw_input("Codigo: ")
nome = raw_input("Nome: ")
endereco = raw_input("Endereco: ")
sexo = raw_input("Sexo: ")
dataNascimento = raw_input("Data de Nascimento: ")

funcionario = {"codigoFuncionario:"codigo,"nome":nome,"endereco":endereco,"sexo":sexo,"datanascimento":dataNascimento}

servico.cadastrarFuncionario(funcionario)


