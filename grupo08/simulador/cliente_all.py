#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
proxy = SOAPProxy("http://localhost:8000")

print str(proxy.consultaProduto("001"))
print str(proxy.consultarCliente("001"))
print str(proxy.consultarFuncionario("001"))

