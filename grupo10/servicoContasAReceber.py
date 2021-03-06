#cadastrarContaAreceber(ContasAreceber)
#ContasArecebe = {codigoAreceber, codigoVenda,dataVencimento,
#dataPagamento, status}
#conssultarAreceber(codigoAreceber)
#deletarAreceber(codigoAreceber)

from SOAPpy import SOAPProxy, SOAPServer
from threading import Thread
arquivo = 'basededados.txt'
#
conta = {'codigoAreceber':'0001','codigoVenda':'0001','dataVencimento':'20/05/2013','dataPagamento':'','status':'pendente'}
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
    
def consultarAreceber(codigoAreceber):
    try:
        conexao = open(arquivo, 'r')
    except:
        return False
    dados = conexao.read()
    linhas = dados.split('\n')
    for linha in linhas:
        if linha == '':
            break
        arrayLinha = linha.split('|')
        if arrayLinha[0] == codigoAreceber:
            return converterLinhaParaDicionario(arrayLinha)
    return False
    
def existeContaParaVenda(codigoVenda):
    try:
        conexao = open(arquivo, 'r')
    except:
        return False
    dados = conexao.read()
    linhas = dados.split('\n')
    for linha in linhas:
        if linha == '':
            break
        arrayLinha = linha.split('|')
        if arrayLinha[1] == codigoVenda:
            return True
    return False
    
def deletarAreceber(codigoAreceber):
    try:
        conexao = open(arquivo, 'r')
    except:
        return False
    dados = conexao.read()
    conexao.close()
    conexao = open(arquivo, 'w')
    linhas = dados.split('\n')
    apagou = False
    for linha in linhas:
        if linha == '':
            break
        arrayLinha = linha.split('|')
        if arrayLinha[0] == codigoAreceber:
            apagou = True
        else:
            conexao.write('%s|%s|%s|%s|%s\n'%(arrayLinha[0],arrayLinha[1],arrayLinha[2],arrayLinha[3],arrayLinha[4]))
    conexao.close()
    return apagou

def converterLinhaParaDicionario(array):
    return {'codigoAreceber':array[0],'codigoVenda':array[1],'dataVencimento':array[2],'dataPagamento':array[3],'status':array[4]}


def iniciarServico():
    serv = SOAPServer(("localhost", 8080))
    serv.registerFunction(cadastrarContaAreceber)
    serv.registerFunction(consultarAreceber)
    serv.registerFunction(deletarAreceber)
    serv.registerFunction(existeContaParaVenda)
    serv.serve_forever()
    print "Servico iniciado"

t = Thread(target=iniciarServico)
t.start()
raw_input("Aperte enter para terminar")
t._Thread__stop()
