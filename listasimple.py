class Nodo:

    def __init__(self, datos):
        self.datos=datos
        self.siguiente=None
        

class listaSimple:
    def __init__(self):
        self.cabeza=None
        self.cabeza2=None
        self.tamaño=0
         

    def insertar(self,datos):
        nuevoNodo=Nodo(datos)
        if self.tamaño == 0:
            self.cabeza = nuevoNodo
            self.tamaño+=1

        else:
            auxiliar=self.cabeza
            auxiliar2=self.cabeza
            contador=0
            while auxiliar.siguiente !=None:
                while auxiliar2 !=None:
                    if nuevoNodo.datos == auxiliar2.datos:
                        contador+=1
                        auxiliar2=auxiliar2.siguiente
                    else:
                        auxiliar2=auxiliar2.siguiente
                auxiliar=auxiliar.siguiente
            if contador==0:
                auxiliar.siguiente=nuevoNodo
                self.tamaño+=1

    def buscar(self,nombre_cel):
        aux=self.cabeza
        while aux !=None:
            if aux.nombre_cel == nombre_cel:
                print("")
            aux=aux.siguiente
