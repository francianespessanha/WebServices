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
            
            codigoFuncinario,nome,endereco,sexo,datanascimento = linha.split("|")
            codigoFuncinario = int(codigoFuncinario)
            
            if codigo==codigoFuncinario:
                dados = {"codigoFuncinario":codigoFuncinario, "nome":nome, "endereco":endereco, "sexo":sexo, "datanascimento":datanascimento}
                return dados
            
        return False
        

    def cadastrarFuncionario(self,dados):
        if self.consultarFuncionario(dados["codigoFuncinario"]):
            return False
        
        conexao = open(self.db,"a")
        conexao.write("%s|%s|%s|%s|%s\n" %(dados["codigoFuncinario"],dados["nome"],dados["endereco"],dados["sexo"],dados["datanascimento"]))
        conexao.close()
        return True    
        
        
    def deletarFuncinario(self,codigo,qtdVendas):
        if qtdVendas > 0:
            return False
        else:
            #procedimento para excluir o funcionario
            return True
