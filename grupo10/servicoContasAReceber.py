#cadastrarContaAreceber(ContasAreceber)
#ContasArecebe = {codigoAreceber, codigoVenda,dataVencimento,
#dataPagamento, status}

#conssultarAreceber(codigoAreceber)
#deletarAreceber(codigoAreceber)

#from SOAPpy import SOAPProxy
arquivo = 'basededados.txt'
#conta = {'codigoAreceber':'0001','codigoVenda':'0001','dataVencimento':'20/05/2013','dataPagamento':'','status':'pendente'}
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
    
def deletarAreceber(codigoAreceber):
    pass

def converterLinhaParaDicionario(array):
    return {'codigoAreceber':array[0],'codigoVenda':array[1],'dataVencimento':array[2],'dataPagamento':array[3],'status':array[4]}