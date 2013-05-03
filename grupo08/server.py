#{codigoVenda,codigoCliente,codigoFuncionario,data,valortotal,					   {codigoProduto,quantidade}}


from SOAPpy import SOAPProxy, SOAPServer
from decimal import Decimal
from datetime import date


server_all = SOAPProxy("http://localhost:8000")

#cliente = SOAPProxy("http://localhost:8005")

#funcionario = SOAPProxy("http://localhost:8007")

#produto = SOAPProxy("http://localhost:8002")


def cadastrarVenda(codigoCliente, codigoFuncionario, codigoProduto, quantidade):
    
    #testar se cliente informado existe - trocar server_all por cliente, funcionario e produto respectivamente
    if server_all.consultarCliente(codigoCliente) is not None and server_all.consultarFuncionario(codigoFuncionario) is not None and server_all.consultaProduto(codigoProduto) is not None:
        produto = server_all.consultaProduto(codigoProduto)
        valor_total = Decimal(produto[2]) * int(quantidade)
        data = str(date.today())
        venda = open("venda.txt", "a+")
        lista = venda.readlines()
         
        if len(lista) > 0:       
            codigo_venda = int(lista[-1].split("|")[0])+1
        else:
            codigo_venda = len(venda.readlines()) + 1
        venda.write("%3.3d" % codigo_venda + "|" + str(codigoCliente) + "|" + str(codigoFuncionario) + "|" + str(data) + "|" + str(valor_total) + "|" + str(codigoProduto) + "|" + str(quantidade)+ "\n")
        venda.close()
        return "Venda cadastrada."
        
    elif server_all.consultarCliente(codigoCliente) is None:
        return "Cliente inexistente"
    
    elif server_all.consultarFuncionario(codigoFuncionario) is None:
        return "Funcionario inexistente"
        
    elif server_all.consultaProduto(codigoProduto) is None:
        return "Produto inexistente"
    
    
def consultarVenda(codigoVenda):
    venda = open("venda.txt", "r")
    consulta = None
    for v in venda.readlines():
        if codigoVenda == v.split("|")[0]:
            consulta = v.split("|")
    venda.close()
    return consulta             
    

def deletarVenda(codigoVenda):
        
    venda = open("venda.txt", "r")
    exclusao = "Venda inexistente. Exclusao abortada."
    resultado = ''
    for v in venda.readlines():
        if codigoVenda == v.split("|")[0]:
            exclusao = "Venda deletada."
        else:
            resultado += "".join(v)    
    venda.close()
    venda = open("venda.txt", "w")
    venda.write(resultado)
    venda.close()
    return exclusao


def consultaVendaCliente(codigo_cliente):
    venda = open("venda.txt", "r")
    consulta = False
    for v in venda.readlines():
        if codigo_cliente == v.split("|")[1]:
            consulta = True
    venda.close()
    return consulta
    
    
serv = SOAPServer(("localhost", 8008))
serv.registerFunction(cadastrarVenda)
serv.registerFunction(consultarVenda)
serv.registerFunction(deletarVenda)
serv.registerFunction(consultaVendaCliente)
print "Servidor de vendas inicializado!!!"
serv.serve_forever()
