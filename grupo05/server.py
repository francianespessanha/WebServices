#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer
banco = 'clientes.txt'

def cadastrar(cliente):
    if consultaCliente(cliente):
        return False
	 codigo = rand(10)
    arquivo = open(banco,'a')
    arquivo.write('%s|%s\n' %
  (cliente['codigo'],cliente['nome'],cliente['contato']))
    arquivo.close()
    return True

def consultaCliente(cliente):

	arquivo = open(banco,'r')
	arquivo.read()

	for arquivo in arquivos.split('\n'):        
		if arquivo == '':
			break
		codigo,nome,contato = arquivo.split('|')
	return codigo
	return nome
	return contato	
	


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

