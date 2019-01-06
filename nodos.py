from tabla_simbolos import *
from scanner import *
from tabla_simbolos_visitor import *

class Nodo():
    pass

#Inicio

class Programa(Nodo):
    def __init__(self, lista_decl_p):
        self.lista_decl1 = lista_decl_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_programa(self)

    def accept2(self, build):
        build.visit_programa(self)



#Dependiendo de lo que se envíe en Parser.py, serán los terminales y no terminales enviados en cada método.
#No terminales: _t
#Terminales: _p


#Con el fin de simplificar nodos, se hacen IF para analizar cada caso según corresponda, y diferencias hacia cuál camino  dirigirse


class DeclaracionVar(Nodo):
    def __init__(self, def_tipo_p, ID_t, NUM_t):
        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        if NUM_t is not ';':
            self.NUM_t = NUM_t
        else:
            self.NUM_t = None
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_declaracion_var(self)

    def accept2(self, build):
        build.visit_declaracion_var(self)

class DeclaracionFun(Nodo):
    def __init__(self, def_tipo_p, ID_t, parametros_p, sentencia_comp_p):
        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.parametros_p = parametros_p
        self.sentencia_comp_p = sentencia_comp_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_declaracion_fun(self)

    def accept2(self, build):
        build.visit_declaracion_fun(self)


#Cuando un camino está contenido en otro, se debe analizar algún caso para diferenciarlos, y así saber donde derivar


class Param(Nodo):
    def __init__(self, def_tipo_p, ID_t, LESSTHAN_t, GREATERTHAN_t):
        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        if LESSTHAN_t is not None:
            self.LESSTHAN_t = LESSTHAN_t
            self.GREATERTHAN_t = GREATERTHAN_t
        else:
            self.LESSTHAN_t = None
            self.GREATERTHAN_t = None
        self.tabla_simbolos = None


    def accept(self, visitor):
        visitor.visit_param(self)

    def accept2(self, build):
        build.visit_param(self)

class SentenciaComp(Nodo):
    def  __init__(self, PARENTESISIZQ_t, declaraciones_locales_p, lista_sentencias1_p, PARENTESISDER_t):
        self.PARENTESISIZQ_t = PARENTESISIZQ_t
        self.declaraciones_locales_p = declaraciones_locales_p
        self.lista_sentencias1_p = lista_sentencias1_p
        self.PARENTESISDER_t = PARENTESISDER_t
        self.tabla_simbolos = None


    def accept(self, visitor):
        visitor.visit_sentencia_comp(self)

    def accept2(self, build):
        build.visit_sentencia_comp(self)

class DeclaracionesLocales(Nodo):
    def __init__(self, declaraciones_locales_p, declaraciones_variables_p, argumentos2_p):
        self.declaraciones_locales_p = declaraciones_locales_p
        self.declaraciones_variables_p = declaraciones_variables_p
        self.argumentos2_p = argumentos2_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_declaraciones_locales(self)

    def accept2(self, build):
        build.visit_declaraciones_locales(self)


class SentenciaSeleccion(Nodo):
    def __init__(self, SI_t, CORCHETEIZQ_t, expresion_p, CORCHETEDER_t, sentencia1_p, SINO_t, sentencia2_p):
        self.SI_t = SI_t
        self.CORCHETEIZQ_t = CORCHETEIZQ_t
        self.expresion_p = expresion_p
        self.CORCHETEDER_t = CORCHETEDER_t
        self.sentencia1_p = sentencia1_p
        if SINO_t is not None:
            self.SINO_t = SINO_t
            self.sentencia2_p = sentencia2_p
        else:
            self.SINO_t = None
            self.sentencia2_p = None
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_sentencia_seleccion(self)

    def accept2(self, build):
        build.visit_sentencia_seleccion(self)

class SentenciaIteracion1(Nodo):
    def __init__(self, MIENTRAS_t, CORCHETEIZQ_t, expresion_p, CORCHETEDER_t, sentencia_p):
        self.MIENTRAS_t = MIENTRAS_t
        self.CORCHETEIZQ_t = CORCHETEIZQ_t
        self.expresion_p = expresion_p
        self.CORCHETEDER_t = CORCHETEDER_t
        self.sentencia_p = sentencia_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_sentencia_iteracion1(self)

    def accept2(self, build):
        build.visit_sentencia_iteracion1(self)

class SentenciaIteracion2(Nodo):
    def __init__(self, REP_t, sentencia_comp_p):
        self.REP_t = REP_t
        self.sentencia_comp_p = sentencia_comp_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_sentencia_iteracion2(self)

    def accept2(self, build):
        build.visit_sentencia_iteracion2(self)

class SentenciaRetorno(Nodo):
    def __init__(self, RET_t, expresion_p):
        self.RET_t = RET_t
        self.expresion_p = expresion_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_sentencia_retorno(self)

    def accept2(self, build):
        build.visit_sentencia_retorno(self)

class Expresion(Nodo):
    def __init__(self, var_p, expresion1_p):
        self.var_p = var_p
        self.expresion1_p = expresion1_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_expresion(self)

    def accept2(self, build):
        build.visit_expresion(self)

class Var(Nodo):
    def __init__(self, ID_t, LESSTHAN_t, expresion1_p, GREATERTHAN_t):
        self.ID_t = ID_t
        self.LESSTHAN_t = LESSTHAN_t
        self.expresion1_p = expresion1_p
        self.GREATERTHAN_t = GREATERTHAN_t
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_var(self)

    def accept2(self, build):
        build.visit_var(self)

class ExpresionNegada(Nodo):
    def __init__(self, NOT_t, CORCHETEIZQ_t, expresion_logica_p, CORCHETEDER_t):
        self.NOT_t = NOT_t
        self.CORCHETEIZQ_t = CORCHETEIZQ_t
        self.expresion_logica_p = expresion_logica_p
        self.CORCHETEDER_t = CORCHETEDER_t
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_expresion_negada(self)

    def accept2(self, build):
        build.visit_expresion_negada(self)

class ExpresionLogica(Nodo):
    def __init__(self, expresion_logica_p, AND_t, NOT_t, CORCHETEIZQ_t, expresion_simple_p, CORCHETEDER_t):

        if expresion_logica_p is not None:
            self.expresion_logica_p = expresion_logica_p
            self.AND_t = AND_t
            if NOT_t is not None:
                self.NOT_t = NOT_t
                self.CORCHETEIZQ_t = CORCHETEIZQ_t
                self.expresion_simple_p = expresion_simple_p
                self.CORCHETEDER_t = CORCHETEDER_t
            else:
                self.NOT_t = None
                self.CORCHETEIZQ_t = None
                self.expresion_simple_p = expresion_simple_p
                self.CORCHETEDER_t = None
        else:
            self.NOT_t = None
            self.CORCHETEIZQ_t = None
            self.expresion_simple_p = expresion_simple_p
            self.CORCHETEDER_t = None
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_expresion_logica(self)

    def accept2(self, build):
        build.visit_expresion_logica(self)

class ExpresionSimple(Nodo):
    def __init__(self, expresion_simple_p, relop_p, expresion_aditiva_p):
        self.expresion_simple_p = expresion_simple_p
        self.relop_p = relop_p
        self.expresion_aditiva_p = expresion_aditiva_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_expresion_simple(self)

    def accept2(self, build):
        build.visit_expresion_simple(self)


class ExpresionAditiva(Nodo):
    def __init__(self, expresion_aditiva_p, addop_p, term_p):
        self.expresion_aditiva_p = expresion_aditiva_p
        self.addop_p = addop_p
        self.term_p = term_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_expresion_aditiva(self)

    def accept2(self, build):
        build.visit_expresion_aditiva(self)

class Term(Nodo):
    def __init__(self, term_p, mulop_p, factor_p):
        self.term_p = term_p
        self.mulop_p = mulop_p
        self.factor_p = factor_p
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_term(self)

    def accept2(self, build):
        build.visit_term(self)

class Factor(Nodo):
    def __init__(self, CORCHETEIZQ_t, expresion_p, CORCHETEDER_t):
        self.CORCHETEIZQ_t = CORCHETEIZQ_t
        self.expresion_p = expresion_p
        self.CORCHETEDER_t = CORCHETEDER_t
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_factor(self)

    def accept2(self, build):
        build.visit_factor(self)


class Invocacion(Nodo):
    def __init__(self, ID_t, PARENTESISIZQ_t, argumentos_p, PARENTESISDER_t):
        self.ID_t = ID_t
        self.PARENTESISIZQ_t = PARENTESISIZQ_t
        self.argumentos_p = argumentos_p
        self.PARENTESISDER_t = PARENTESISDER_t
        self.tabla_simbolos = None

    def accept(self, visitor):
        visitor.visit_invocacion(self)

    def accept2(self, build):
        build.visit_invocacion(self)
