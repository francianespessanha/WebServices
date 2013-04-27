#cadastrarContaAreceber(ContasAreceber)
#ContasArecebe = {codigoAreceber, codigoVenda,dataVencimento,
#dataPagamento, status}

#conssultarAreceber(codigoAreceber)
#deletarAreceber(codigoAreceber)

#from SOAPpy import SOAPProxy
arquivo = 'usuarios.txt'

def cadastrarContaAreceber(contasAReceber):
    contasAReceber['codigoAreceber']
    #servico = SOAPProxy("http://localhost:8080")
    #venda = servico.consultarVenda(contasAReceber['codigoVenda'])
    venda = True
    if venda:
        #gravar venda
        conexao = open(arquivo,'a')
        conexao.write('%s|%s|%s|%s|%s\n' %(contasAReceber['codigoAreceber'],
                                           contasAReceber['codigoVenda'],
                                           contasAReceber['dataVencimento'],
                                           contasAReceber['dataPagamento'],
                                           contasAReceber['status']))
        conexao.close()
        return True
    else:
        #venda nao existe
        return False
    
def conssultarAreceber(codigoAreceber):
    pass
    
def deletarAreceber(codigoAreceber):
    pass
