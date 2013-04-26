<<<<<<< HEAD

from SOAPpy import SOAPServer
db = 'Funcionario.txt'
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
    if consultarFuncionario(Funcionario):
        return False
    conexao = open(db,'a')
    conexao.write('%d|%s|%s|%s|%s\n' %(funcionario['codigoFuncionario'],nome['nome'], endereco['endereco'],sexo['sexo'],datanascimento['datanascimento']))
    conexao.close()
    return True

serv = SOAPServer(("localhost", 8080))
serv.registerFunction(consultarFuncionario)
serv.registerFunction(cadastrarFuncionario)

serv.serve_forever()
=======
#encoding:utf-8

from SOAPpy import SOAPServer

server = SOAPServer(("localhost",8080))




>>>>>>> 24834b54d569b2d183d0550eae357e9d7e15c7bc
