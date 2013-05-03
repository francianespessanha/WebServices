from SOAPpy import SOAPServer


def consultaProduto(codigoProduto):
    produto = open("produto.txt", "r")
    consulta = None
    for p in produto.readlines():
        if codigoProduto == p.split(",")[0]:
            consulta = p.split(",")
    return consulta

def consultarCliente(codigoCliente):
    cliente = open("cliente.txt", "r")
    consulta = None
    for c in cliente.readlines():
        if codigoCliente == c.split(",")[0]:
            consulta = c.split(",")
    return consulta

def consultarFuncionario(codigoFuncionario):
    funcionario = open("funcionario.txt", "r")
    consulta = None
    for f in funcionario.readlines():
        if codigoFuncionario == f.split(",")[0]:
            consulta = f.split(",")
    return consulta

    
    
serv = SOAPServer(("localhost", 8000))
serv.registerFunction(consultaProduto)
serv.registerFunction(consultarCliente)
serv.registerFunction(consultarFuncionario)
print "server all inicializado..."
serv.serve_forever()


