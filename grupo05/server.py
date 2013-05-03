#-*- encoding: iso-8859-1 -*-
# -*- coding: utf-8 -*-

from SOAPpy import SOAPServer
banco = 'clientes.txt'

def cadastrar(cliente):
	if consultaCliente(cliente):
    		return False
	arquivo = open(banco,'a')
	arquivo.write('%s|%s|%s\n' %(cliente['codigo'],
    					cliente['nome'],
					cliente['contato']
					)
				)
    	arquivo.close()
    	return arquivo 

def consultaCliente(codigo1):
	arquivos = open(banco,'r').read().split('\n')
	for arquivo in arquivos:        
		if arquivo == '':
			print "Vazio"
			break
		codigo,nome,contato = arquivo.split('|')
		dic = {}
		dic['codigo'] = codigo
		dic['nome'] = nome
		dic['contato'] = contato
		if dic['codigo'] == codigo1:
			return dic.items()
	

def deletaCliente(codigoCliente):
#	Procurar onde está o proxy vendas	
#	if cod true
#		return false
	if consultaCliente(codigoCliente):
		return False
	arquivos = open(banco,'r').read().split('\n')
	for line in arquivos:
		


serv = SOAPServer(("localhost", 8005))
serv.registerFunction(cadastrar)
serv.registerFunction(consultaCliente)
serv.serve_forever()

