#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer
banco = 'clientes.txt'

def cadastrar(cliente):
#    if consultaCliente(cliente):
#    	return False

    arquivo = open(banco,'a')
    arquivo.write('%s|%s|%s\n' %(cliente['codigo'],
    				cliente['nome'],
				cliente['contato']
				)
			)
    arquivo.close()
    return arquivo 

def consultaCliente(codigo1):
	arquivo= {}
	arquivos = open(banco,'r').readlines()

	for arquivo in arquivos:        
		if arquivo == '':
			print "Vazio"
			break
		codigo,nome,contato = arquivo.split('|')
		if codigo['codigo'] == codigo1:
			return True
			print codigo,nome, contato
	


#def deletaCliente(codigoCliente):
#	Procurar onde está o proxy vendas	
#	if cod true
#		return false
#	else
#		codigo deleta venda


serv = SOAPServer(("localhost", 8005))
serv.registerFunction(cadastrar)
serv.registerFunction(consultaCliente)
serv.serve_forever()

