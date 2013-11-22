class arvore():
    def __init__(self):
        self.pRaiz = None

    def buscaRec(self, subRaiz, cod):
        if subRaiz != None:
            if subRaiz.codigo == cod:
                print "\n %d encontrado" %cod
                return
            else:
                if subRaiz.codigo > cod:
                    self.buscaRec(subRaiz.pFilhoMenor, cod)
                else:
                    self.buscaRec(subRaiz.pFilhoMaior, cod)
        else:
            print "\n%d nao encontrado" %cod

    def busca(self, cod):
        if self.pRaiz == None:
            print "\n Arvore vazia"
        else:
            noAtual = self.pRaiz
            while(True):
                if noAtual.codigo == cod:
                    print "\n%d encontrado" %cod
                    break
                elif noAtual.codigo > cod:
                    noAtual = noAtual.pFilhoMenor
                else:
                    noAtual = noAtual.pFilhoMaior
                if noAtual == None:
                    print "\n%d nao encontrado" %cod
                    break

    def inserir(self, cod, desc):
        novoElem = itemDaArvore(cod,desc)
        if self.pRaiz == None:
            self.pRaiz = novoElem
        else:
            pPai = self.pRaiz
            while (True):
                if pPai.codigo > cod and pPai.pFilhoMenor == None:
                    pPai.pFilhoMenor = novoElem
                    novoElem.pai = pPai
                    break
                elif pPai.codigo < cod and pPai.pFilhoMaior == None:
                    pPai.pFilhoMaior = novoElem
                    novoElem.pai = pPai
                    break
                elif pPai.codigo > cod:
                    pPai = pPai.pFilhoMenor
                else:
                    pPai = pPai.pFilhoMaior

            while pPai!= None:
                pPai.atualizaAltura()
                self.balancear(pPai)
                pPai = pPai.pai


    def rotacionarDireita(self, no):
        noAux = no.pFilhoMenor
        if no.pai != None:
            if no.pai.pFilhoMenor == no:
                no.pai.pFilhoMenor = no.pFilhoMenor
            else:
                no.pai.pFilhoMaior = no.pFilhoMenor
            no.pFilhoMenor.pai = pai
        else:
            self.pRaiz = noAux
            noAux.pai = None
        if noAux.pFilhoMaior != None:
            noAux.pFilhoMaior.pai = no
        no.pFilhoMenor = noAux.pFilhoMaior
        noAux.pFilhoMaior = no
        no.pai = noAux
        # Atualizar alturas
        no.atualizaAltura()
        noAux.atualizaAltura()
        if no.pai != None:
            no.pai.atualizaAltura()

    def rotacionarEsquerda(self, no):
        noAux = no.pFilhoMaior
        if no.pai != None:
            if no.pai.pFilhoMaior == no:
                no.pai.pFilhoMaior = no.pFilhoMaior
            else:
                no.pai.pFilhoMaior = no.pFilhoMenor
            no.pFilhoMenor.pai = pai
        else:
            self.pRaiz = noAux
            noAux.pai = None
        if noAux.pFilhoMaior != None:
            noAux.pFilhoMaior.pai = no
        no.pFilhoMaior = noAux.pFilhoMenor
        noAux.pFilhoMenor = no
        no.pai = noAux
        # Atualizar alturas
        no.atualizaAltura()
        noAux.atualizaAltura()
        if no.pai != None:
            no.pai.atualizaAltura()


    def balancear(self, noAtual):
        balanco = noAtual.balanco()
        print noAtual, balanco
        if balanco > 1:
            if noAtual.pFilhoMenor.balanco() < 0:
                print noAtual, "rotacionar esquerda"
            print noAtual, "rotacionando direita"
            self.rotacionarDireita(noAtual)
        elif balanco < -1:
            if noAtual.pFilhoMaior.balanco() > 0:
                print noAtual, "rotacionar direita"
            print noAtual, "rotacionar esquerda"
            self.rotacionarEsquerda(noAtual)

    def pegarMenorMaiores(self,pai, subRaiz):
        if subRaiz.pFilhoMenor == None:
            if pai.codigo > subRaiz.codigo:
                pai.pFilhoMenor = subRaiz.pFilhoMaior
            else:
                pai.pFilhoMaior = subRaiz.pFilhoMaior
            return subRaiz
        else:
            return self.pegarMenorMaiores(subRaiz, subRaiz.pFilhoMenor)

    def remover(self, pai, elemento, cod):
        if elemento.codigo == cod:
            # Caso dos nos sem filhos"
            if elemento.pFilhoMenor == None and elemento.pFilhoMaior == None:
                if pai == None:
                    self.pRaiz = None
                elif pai.codigo > cod:
                    pai.pFilhoMenor = None
                else:
                    pai.pFilhoMaior = None
                    
                pai.atualizaAltura()
                noAtual = pai
                while (noAtual):
					self.balancear(noAtual)
					noAtual = noAtual.pai 	    

            # Caso dos nos com unico filho
            elif elemento.pFilhoMenor == None or elemento.pFilhoMaior == None:
                if pai == None:
                    self.pRaiz = elemento.pFilhoMaior if elemento.pFilhorMaior is not None else elemento.pFilhoMenor
                elif pai.codigo > cod:
                    pai.pFilhoMenor = elemento.pFilhoMaior if elemento.pFilhoMaior is not None else elemento.pFilhoMenor
                else:
                    pai.pFilhoMaior = elemento.pFilhoMaior if elemento.pFilhoMaior is not None else elemento.pFilhoMenor

            # Caso dos nos com dois filhos
            # Estrategia: substituir por menor dos maiores
            else:
                substituto = self.pegarMenorMaiores(elemento, elemento.pFilhoMaior)
                substituto.pFilhoMenor = elemento.pFilhoMenor
                substituto.pFilhoMaior = elemento.pFilhoMaior
                if pai == None:
                    self.pRaiz = substituto
                elif pai.codigo > cod:
                    pai.pFilhoMenor = substituto
                else:
                    pai.pFilhoMaior = substituto

        elif elemento.codigo > cod:
            self.remover(elemento, elemento.pFilhoMenor, cod)
        else:
            self.remover(elemento, elemento.pFilhoMaior, cod)

    def mostrarRaiz(self):
        print self.pRaiz
        print self.pRaiz.pFilhoMenor

    def percorrerInOrder(self, subRaiz):
        if subRaiz != None:
            self.percorrerInOrder(subRaiz.pFilhoMenor)
            print subRaiz.codigo,
            self.percorrerInOrder(subRaiz.pFilhoMaior)

    def percorrerPreOrder(self, subRaiz):
        if subRaiz != None:
            print subRaiz.codigo,
            self.percorrerPreOrder(subRaiz.pFilhoMenor)
            self.percorrerPreOrder(subRaiz.pFilhoMaior)

    def percorrerPosOrder(self, subRaiz):
        if subRaiz != None:
            self.percorrerPosOrder(subRaiz.pFilhoMenor)
            self.percorrerPosOrder(subRaiz.pFilhoMaior)
            print subRaiz.codigo,

class itemDaArvore():
    def __init__(self, cod, desc):
        self.codigo = cod  # index
        self.descricao = desc
        self.pFilhoMaior = None
        self.pFilhoMenor = None
        self.pai = None
        self.altura = 0

    def atualizaAltura(self):
        if self.pFilhoMenor != None and self.pFilhoMaior != None:
            if self.pFilhoMenor.altura > self.pFilhoMaior.altura:
                self.altura = self.pFilhoMenor.altura + 1
            else:
                self.altura = self.pFilhoMaior.altura + 1
        elif self.pFilhoMenor != None:
            self.altura = self.pFilhoMenor.altura + 1
        elif self.pFilhoMaior != None:
            self.altura = self.pFilhoMaior.altura + 1
        else:
            self.altura = 0

    def balanco(self):
        if self.pFilhoMenor != None and self.pFilhoMaior != None:
            return self.pFilhoMenor.altura - self.pFilhoMaior.altura
        elif self.pFilhoMenor != None:
            return self.pFilhoMenor.altura + 1
        elif self.pFilhoMaior != None:
            return (-1) * (self.pFilhoMaior.altura + 1)
        else:
            return 0

    def __str__(self):
        return "Elemento: %d - %s (%d)" %(self.codigo, self.descricao, self.altura)

if __name__=='__main__':
    minhaArvore = arvore()
    minhaArvore.inserir(30,"Trinta")
    minhaArvore.inserir(20,"Vinte")
    minhaArvore.inserir(10,"Quinze")
    minhaArvore.inserir(25,"Oito")
    minhaArvore.inserir(50,"Oito")
    minhaArvore.inserir(52,"Oito")
    minhaArvore.inserir(32,"Oito")
    minhaArvore.inserir(38,"Oito")
    
    minhaArvore.remover(None, minhaArvore.pRaiz, 20)
    
    print "Percorrendo em ordem"
    minhaArvore.percorrerInOrder(minhaArvore.pRaiz)
    print "\nPercorrendo pre ordem"
    minhaArvore.percorrerPreOrder(minhaArvore.pRaiz)
    print "\nPercorrendo pos ordem"
    minhaArvore.percorrerPosOrder(minhaArvore.pRaiz)

