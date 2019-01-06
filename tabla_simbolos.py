# Esto contiene todas las Funciones y Variables Globales
class NodoGeneral(object):
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

        print('Variable Global')
        for i in range(len(self.listGlobales)):
            print(self.listGlobales[i].getID())

        print('Variable Funcion')
        for i in range(len(self.listFuncion)):
            print(self.listFuncion[i].getID())
            nodoFuncion.iterarFuncion(self.listFuncion[i])

#Objeto Variable Global
class nodoVariableGlobal(object):
    def __init__(self, def_tipo, ID, esArreglo):
        self.def_tipo = def_tipo
        self.ID = ID
        self.esArreglo = esArreglo

    def getDefTipo(self):
        return self.def_tipo

    def getID(self):
        return self.ID

    def getArreglo(self):
        return self.esArreglo

# Objeto Funcion
class nodoFuncion(object):
    def __init__(self, def_tipo, ID):
        self.def_tipo = def_tipo
        self.ID = ID
        self.listLocales = []
        self.listParam = []
        self.listBloque = []


    def getID(self):
        return self.ID

    def agregarParam(self, Nodo):
        self.listParam.append(Nodo)

    def agregarLocales(self, Nodo):
        self.listLocales.append(Nodo)

    def iterarFuncion(self):

        print('->Variable Parametros')
        for i in range(len(self.listParam)):
            print("    *", self.listParam[i].getID())


        print('->Variable Locales')
        for i in range(len(self.listLocales)):
            print("    *", self.listLocales[i].getID())

#Objeto Variable Parámetro
class nodoVariableParam(object):
    def __init__(self, def_tipo, ID, esArreglo):
        self.def_tipo = def_tipo
        self.ID = ID
        self.esArreglo = esArreglo

    def getDefTipo(self):
        return self.def_tipo

    def getID(self):
        return self.ID

    def getArreglo(self):
        return self.esArreglo

# Objeto Variable Local
class nodoVariableLocal(object):
    def __init__(self, def_tipo, ID, esArreglo):
        self.def_tipo = def_tipo
        self.ID = ID
        self.esArreglo = esArreglo

    def getDefTipo(self):
        return self.def_tipo

    def getID(self):
        return self.ID

    def getArreglo(self):
        return self.esArreglo
