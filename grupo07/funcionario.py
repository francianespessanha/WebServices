from SOAPpy import SOAPServer
db = 'Funcionarios.txt'
def consultarFuncionario(codigoFuncionario):
    try:
        linhas = open(db,'r').read()
    except:
        return False
    
    for linha in linhas.split('\n'):
        
        if linha == '':
           break 
        codigoFuncionario,nome,endereco,sexo,datanascimento = linha.split('|')
        if codigoFuncionario['codigoFuncionario'] == codigoFuncionario:
            return True
    return False

def cadastrarFuncionario(Funcionario):
    if consultarFuncionario(Funcionario[0]):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s|%s|%s|%s\n' %(funcionario['codigoFuncionario'],nome['nome'], endereco['endereco'],sexo['sexo'],datanascimento['datanascimento']))
    conexao.close()
    return True

def deletarFuncionario(codigo):
    if consultarFuncionario(codigo):
        return False


serv = SOAPServer(("localhost", 8087))
serv.registerFunction(consultarFuncionario)
serv.registerFunction(cadastrarFuncionario)
serv.registerFunction(deletarFuncionario)

serv.serve_forever()
