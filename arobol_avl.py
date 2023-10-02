from nodo_avl import Nodo_AVL
import os

class Arbol_AVL():
    def __init__(self):
        self.raiz = None

    def Insertar(self,valor):
        self.raiz=self.InsertarNodo(valor,self.raiz)

    def altura_nodo(self,raiz):
        condicion= raiz ==None
        return 0 if condicion else raiz.altura
    
    def equilibrio_nodo(self, raiz):
        condicion = raiz == None
        return 0 if condicion else (self.altura_nodo(raiz.derecho) - self.altura_nodo(raiz.izquierdo))
    
    def RotacionI(self,raiz):
        raiz_derecho = raiz.derecho
        hijo_izquierdo = raiz_derecho.izquierdo
        raiz_derecho.izquierdo = raiz
        raiz.derecho = hijo_izquierdo
        raiz.altura = 1 + max(self.altura_nodo(raiz.izquierdo),self.altura_nodo(raiz.derecho))
        raiz.factor_equilibrio = self.equilibrio_nodo(raiz)
        raiz_derecho.altura = 1 + max(self.altura_nodo(raiz_derecho.izquierdo),self.altura_nodo(raiz_derecho.derecho))
        raiz_derecho.factor_equilibrio = self.equilibrio_nodo(raiz_derecho)
        return raiz_derecho
    
    def RotacionD(self, raiz):
        raiz_izquierdo = raiz.izquierdo
        hijo_derecho = raiz_izquierdo.derecho
        raiz_izquierdo.derecho = raiz
        raiz.izquierdo = hijo_derecho
        raiz.altura = 1 + max(self.altura_nodo(raiz.izquierdo), self.altura_nodo(raiz.derecho))
        raiz.factor_equilibrio = self.equilibrio_nodo(raiz)
        raiz_izquierdo.altura = 1 + max(self.altura_nodo(raiz_izquierdo.izquierdo), self.altura_nodo(raiz_izquierdo.derecho))
        raiz_izquierdo.factor_equilibrio = self.equilibrio_nodo(raiz_izquierdo)
        return raiz_izquierdo

    def InsertarNodo(self, valor, raiz):
        if raiz is None:
            return Nodo_AVL(valor)
        else:
            if raiz.valor == valor:
                raiz.valor = valor
            elif raiz.valor > valor:
                raiz.izquierdo = self.InsertarNodo(valor, raiz.izquierdo)
            elif raiz.valor < valor:
                raiz.derecho = self.InsertarNodo(valor, raiz.derecho)
        #Luego de insercion, procedemos a realizar rotaciones
        raiz.altura = 1 + max(self.altura_nodo(raiz.izquierdo),self.altura_nodo(raiz.derecho))
        balanceo = self.equilibrio_nodo(raiz)
        raiz.factor_equilibrio = balanceo

        if balanceo > 1 and valor > raiz.derecho.valor:#Rotacion Simple a la Izquierda
            return self.RotacionI(raiz)
        if balanceo < -1 and valor < raiz.izquierdo.valor:#Rotacion Simple a la Derecha
            return self.RotacionD(raiz)
        if balanceo > 1 and valor < raiz.derecho.valor:#Rotacion Doble a la Izquierda
            raiz.derecho = self.RotacionD(raiz.derecho)
            return self.RotacionI(raiz)
        if balanceo < -1 and valor > raiz.izquierdo.valor:#Rotacion Doble a la Derecha
            raiz.izquierdo = self.RotacionI(raiz.izquierdo)
            return self.RotacionD(raiz)
        return raiz
    
    def recorridoInorden(self):
        self.Inorden(self.raiz)

    def Inorden(self, raiz):
        if raiz is not None:
            self.Inorden(raiz.izquierdo)
            print(raiz.valor, end=' ')
            self.Inorden(raiz.derecho)

    def recorridoPreOrden(self):
        self.PreOrden(self.raiz)
    
    def PreOrden(self, raiz):
        if raiz is not None:
            print(raiz.valor, end=' ')
            self.PreOrden(raiz.izquierdo)
            self.PreOrden(raiz.derecho)

    def recorridoPostOrden(self):
        self.PostOrden(self.raiz)

    def PostOrden(self, raiz):
        if raiz is not None:
            self.PostOrden(raiz.izquierdo)
            self.PostOrden(raiz.derecho)
            print(raiz.valor, end=' ')

    def graficar(self):
        cadena = ''
        archivo = "arbolAVL.jpg"
        a = open("arbolAVL.dot","w")
        if self.raiz is not None:
            cadena += "digraph arbol {"
            cadena += self.retornarValoresArbol(self.raiz, 0)
            cadena += "}"
        a.write(cadena)
        a.close()
        os.system("dot -Tjpg arbolAVL.dot -o " + archivo)
        #os.system(archivo)


    def retornarValoresArbol(self, raiz, id):
        cadena = ''
        numero = id + 1
        if raiz is not None:
            cadena += "\""
            cadena += str(raiz.valor)
            cadena += "\" ;\n"
            if(raiz.izquierdo is not None and raiz.derecho is not None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"{}\" -> {} \"{}\" -> {}".format(raiz.valor, self.retornarValoresArbol(raiz.izquierdo, numero), raiz.valor, self.retornarValoresArbol(raiz.derecho, numero))
                cadena += "{" + "rank=same" + "\"{}\" -> \"{}\" [style=invis]; ".format(raiz.izquierdo.valor, raiz.derecho.valor) + "} \n"
            elif(raiz.izquierdo is not None and raiz.derecho is None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"{}\" -> {} \"{}\" -> x{}[style=invis];\n".format(raiz.valor, self.retornarValoresArbol(raiz.izquierdo, numero), raiz.valor, numero)
                cadena += "{" + "rank=same " + "\"{}\" -> x{} [style=invis]; ".format(raiz.izquierdo.valor, numero) + "} \n"
            elif(raiz.izquierdo is None and raiz.derecho is not None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"{}\" -> x{}[style=invis]; \n \"{}\" -> {}".format(raiz.valor, numero, raiz.valor, self.retornarValoresArbol(raiz.derecho, numero))
                cadena += "{" + "rank=same " + "x{} -> \"{}\" [style=invis]; ".format(numero, raiz.derecho.valor) + "} \n"
        return cadena
