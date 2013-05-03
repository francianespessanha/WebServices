#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8005")


print ('Menu: \n Escolha opção: \n 1 - Cadastrar \n 2 - Consultar ')
opcao = input('Opção: ')
if opcao == 1:
	codigo = raw_input('Codigo: ')
	nome = raw_input('Nome: ')
	contato = raw_input('Contato: ')
	cliente ={'codigo':codigo,'nome':nome,'contato':contato}
	servico.cadastrar(cliente)
else:
	codigo = raw_input('codigo: ')
	servico.consultaCliente(codigo)
