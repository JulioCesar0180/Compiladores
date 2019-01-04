
class NodoLocales(object):
    def __init__(self, ):
        self.listLocales = []
        self.listParam = []
        self.Padre = None

    def agregarLocales(self, Nodo):
        self.listLocales.append(Nodo)

    def getLocales(self):
        return self.listLocales

class NodoFuncionGlobales(object):
    def __init__(self):
        self.listFuncion = []
        self.listGlobales = []


    def agregarFuncion(self, Nodo):
        self.listFuncion.append(Nodo)

    def agregarGlobal(self, Nodo):
        self.listGlobales.append(Nodo)

    def getFuncion(self):
        return self.listFuncion

    def getGlobales(self):
        return self.listGlobales

    def iterar(self):
        for i in range(len(self.listGlobales)):
            print(self.listGlobales[i].getID(), self.listGlobales[i].getDefTipo(), self.listGlobales[i].getEsArreglo())







class nodoVariableGlobal(object):
    def __init__(self, def_tipo, ID, esArreglo):
        self.def_tipo = def_tipo
        self.ID = ID
        self.esArreglo = esArreglo

    def getDefTipo(self):
        return self.def_tipo

    def getID(self):
        return self.ID

    def getEsArreglo(self):
        return self.esArreglo

