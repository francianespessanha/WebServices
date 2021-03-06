#encoding: utf-8

class Funcionario(object):
    def __init__(self,db):
        self.db = db
        
    def consultarFuncionario(self,codigo):
        try:
            linhas = open(self.db,"r").read()
        except:
            return False
        
        for linha in linhas.split("\n"):
            if linha == "":
                break
            
            codigoFuncionario,nome,endereco,sexo,datanascimento = linha.split("|")
            codigoFuncionario = int(codigoFuncionario)
            
            if codigo==codigoFuncionario:
                dados = {"codigoFuncionario":codigoFuncionario, "nome":nome, "endereco":endereco, "sexo":sexo, "datanascimento":datanascimento}
                return dados
            
        return False
        

    def cadastrarFuncionario(self,dados):
        if self.consultarFuncionario(dados["codigoFuncionario"]):
            return False
        
        conexao = open(self.db,"a")
        conexao.write("%s|%s|%s|%s|%s\n" %(dados["codigoFuncionario"],dados["nome"],dados["endereco"],dados["sexo"],dados["datanascimento"]))
        conexao.close()
        return True    
        
        
    def deletarFuncionario(self,codigo,qtdVendas):
        if qtdVendas > 0:
            return False
        else:
            #procedimento para excluir o funcionario
            return True
