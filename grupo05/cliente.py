#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8005")
codigo = raw_input('Codigo: ')
nome = raw_input('Nome: ')
contato = raw_input('Contato: ')

cliente ={'codigo':codigo,'nome':nome,'contato':contato}
servico.cadastrar(cliente)

codigo1 = raw_input('codigo: ')
servico.consultaCliente(codigo1)

