#coding: utf-8

class Produto:

    def cadastrarProduto(self, descricao, preco, codigofornecedor):
        
        try:
            #if fornecedor.consultarFornecedor(int(codigoFornecedor)) == True:
            if preco == 0 or descricao == "":
                print "\n Erro ao salvar os dados. Os campos devem ser preenchidos! \n"
                return "\n Erro ao salvar os dados. Os campos devem ser preenchidos! \n"
            else:
                self.preco = float(preco)
                self.descricao = descricao
                self.codigofornecedor = int(codigofornecedor)
                produto = []
                temp = self.consultarProduto()
                #print temp
                if (temp[0] != '\n' and temp[-1] != '\n'):
                    x = int(temp[len(temp)-1][1:5]) + 1
                    produto.append("%4.4d"%x)
                    print "%4.4d"%x
                else:
                    produto.append('0001')
                
                produto.append(self.descricao)
                produto.append(self.preco)
                produto.append(self.codigofornecedor)
            
            try:
                arq = open("produtos.txt", "a")
                arq.write(str(produto)+"\n")
                print "\nProduto cadastrado com sucesso!"
                return "\nProduto cadastrado com sucesso!"
            except IOError:
                print "\n Erro ao salvar os dados. A operacao nao pode ser realizada! \n"
                return "\n Erro ao salvar os dados. A operacao nao pode ser realizada! \n"
        except ValueError:
            print "\n Erro ao cadastrar o produto! Dados invalidos! \n"
            return "\n Erro ao cadastrar o produto! Dados invalidos! \n"
    
    def deletarProduto(self, codigoproduto):
        try:
            int(codigoproduto)
            #if estoque.consultarProduto(int(codigoProduto)) == False:
            resultado = self.consultarProduto()
            x = 0
            cont = 0

            while x < len(resultado):
                
                if str(codigoproduto) == resultado[x][1:5]:
                    resultado.pop(x)
                    cont = 1
                x = x + 1

            if cont == 0:
                print "\n A operacao nao pode ser realizada! \n Produto nao encontrado! \n"
                return "\n A operacao nao pode ser realizada! \n Produto nao encontrado! \n"
            else :
                try:
                    arq3 = open("produtos.txt", "w")
                    temp = []
                    x = 0
                    while x < len(resultado):
                        temp.append("["+str(resultado[x])+"]")
                        arq3.write(str(temp[x])+"\n")
                        x = x + 1
                    print "\nProduto excluido com sucesso! \n"
                    return "\nProduto excluido com sucesso! \n"
                except IOError:
                    print "\n Erro ao acessar os dados! \n"
                    return "\n Erro ao acessar os dados! \n"
        except ValueError:
            print "\n Codigo do produto invalido! \n"
            return "\n Codigo do produto invalido! \n"
    
    def consultarProduto(self):
        try:
            arq2 = open("produtos.txt", "r").readlines()
            x = 0
            temp = []
            while x < len(arq2):
                temp.append(str(arq2[x]).replace("\n", "").replace("[", "").replace("]", ""))
                x = x + 1
            if temp == [] or len(temp) == 0:
                #print "Ainda não ha produto cadastrado! \n"
                return "Ainda não ha produto cadastrado! \n"
            return temp
        except IOError:
            print "\n Erro ao acessar os dados! \n"
            return "\n Erro ao acessar os dados! \n"



if __name__ == "__main__":
    produto1 = Produto()
    produto2 = Produto()
    produto1.cadastrarProduto("caneta", 2, 1)
    produto2.cadastrarProduto("lapis", "", 1)
    produto1.deletarProduto(1010)

