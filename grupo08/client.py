#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
proxy = SOAPProxy("http://localhost:8008")


print str(proxy.consultarVenda("001"))
print str(proxy.cadastrarVenda("001", "002", "003", "10"))
print str(proxy.deletarVenda("003"))
print str(proxy.consultaVendaCliente("001"))
