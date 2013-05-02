from SOAPpy import SOAPProxy

sp = SOAPProxy('localhost:8080')

def exibirMenu():
  print "-----MENU-----"
  print ""
  print "1 - Cadastrar"
  print "2 - Consultar"
  print "3 - Apagar"
  print "4 - Sair"
  return input("Escolha uma opcao: ")

def cadastrarConta():
    print "--Cadastro de conta a receber--"
    print ""
    codConta = raw_input("Codigo da conta: ")
    codVenda = raw_input("Codigo da venda: ")
    dtVenc   = raw_input("Dada do vencimento: ")
    dtPag    = raw_input("Data do pagamento: ")
    status   = raw_input("Status: ")
    conta = {'codigoAreceber':codConta,'codigoVenda':codVenda,'dataVencimento':dtVenc,'dataPagamento':dtPag,'status':status}
    try:
        retorno = sp.cadastrarContaAreceber(conta)
    except:
        print "Ocorreu um erro ao tentar gravar a conta"
        return False
    if retorno:
        print "Conta cadastrada com sucesso"
    else:
        print "Ocorreu um erro ao tentar gravar a conta"

def consultarConta():
    print "--Consulta de conta a receber--"
    print ""
    codConta = raw_input("Digite o codigo da conta: ")
    try:
        retorno = sp.consultarAreceber(codConta)
    except:
        print "Ocorreu um erro ao consultar"
        return False
    if retorno:
        print "Conta encontrada"
        print ""
        print "Codigo da conta: %s"%(retorno["codigoAreceber"])
        print "Codigo da venda: %s"%(retorno["codigoVenda"])
        print "Dada do vencimento: %s"%(retorno["dataVencimento"])
        print "Data do pagamento: %s"%(retorno["dataPagamento"])
        print "Status: %s"%(retorno["status"])
    else:
        print "Conta nao encontrada."

def removerConta():
    print "--Apagar conta a receber--"
    print ""
    codConta = raw_input("Digite o codigo da conta: ")
    retorno = sp.deletarAreceber(codConta)
    if retorno:
        print "Conta removida com sucesso"
    else:
        print "Ocorreu um erro ao tentar remover a conta."
 

opcao = 0
while opcao != 4:
    if opcao == 1:
        cadastrarConta()
    if opcao == 2:
        consultarConta() 
    if opcao == 3:
        removerConta() 
    opcao = exibirMenu()
