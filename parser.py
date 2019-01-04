# coding=utf-8

import ply.yacc as yacc

from scanner import tokens

import nodos
from dibujar_AST_visitor import Visitor
from tabla_simbolos import *
from tabla_simbolos_visitor import *

#Código utilizado para resolver los problemas de Shift/Reduce

precedence = (
    ('left', 'SI'),
    ('left', 'SINO')
)


def p_programa(p):
    """program : lista_decl"""
    p[0] = nodos.Programa(p[1])


#Cuando ocurran casos de Recursiones en un mismo nivel, con 2 derivaciones, se usará el algoritmo mostrado a continuación


def p_lista_decl1(p):
    """lista_decl : lista_decl declaracion"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


#En el caso de las derivaciones directas, se usará siempre el algoritmo p[0] = p[1]


def p_lista_decl2(p):
    """lista_decl : declaracion"""
    p[0] = p[1]


def p_declaracion1(p):
    """declaracion : declaracion_var"""
    p[0] = p[1]


def p_declaracion2(p):
    """declaracion : declaracion_fun"""
    p[0] = p[1]


#Para el caso de las derivaciones simultáneas en un mismo nivel, se usará el algoritmo señalado (nodos.Nombrre(p[i]))


def p_declaracion_var1(p):
    """declaracion_var : def_tipo ID PUNTOCOMA"""
    p[0] = nodos.DeclaracionVar(p[1], p[2], p[3])

def p_declaracion_var2(p):
    """declaracion_var : def_tipo ID LESSTHAN NUM GREATERTHAN PUNTOCOMA"""
    p[0] = nodos.DeclaracionVar(p[1], p[2], p[4])

def p_def_tipo1(p):
    """def_tipo : VACUO"""
    p[0] = p[1]

def p_def_tipo2(p):
    """def_tipo : ENT"""
    p[0] = p[1]

def p_declaracion_fun(p):
    """declaracion_fun : def_tipo ID CORCHETEIZQ parametros CORCHETEDER sentencia_comp"""
    p[0] = nodos.DeclaracionFun(p[1], p[2], p[4], p[6])

def p_parametros1(p):
    """parametros : lista_parametros"""
    p[0] = p[1]

def p_parametros2(p):
    """parametros : VACUO"""
    p[0] = p[1]

def p_lista_parametros1(p):
    """lista_parametros : lista_parametros COMA param"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])

def p_lista_parametros2(p):
    """lista_parametros : param"""
    p[0] = p[1]


#Cuando un camino esté contenido dentro de otro, se usarán los None. Como ocurre com Param"


def p_param1(p):
    """param : def_tipo ID"""
    p[0] = nodos.Param(p[1], p[2],None, None)

def p_param2(p):
    """param : def_tipo ID LESSTHAN GREATERTHAN"""
    p[0] = nodos.Param(p[1], p[2], p[3], p[4])

def p_sentencia_comp(p):
    """sentencia_comp : PARENTESISIZQ declaraciones_locales lista_sentencias PARENTESISDER"""
    p[0] = nodos.SentenciaComp(p[1], p[2], p[3], p[4])

def p_declaraciones_locales1(p):
    """declaraciones_locales : declaraciones_locales declaracion_var"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])


#Cuando se deriva a un epsilon, se deriva a Empty


def p_declaraciones_locales2(p):
    """declaraciones_locales : empty"""
    pass

def p_lista_sentencias1(p):
    """lista_sentencias : lista_sentencias sentencia"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]
        # p[0] = nodos.nodoVacio(is_vacio=True, vacio_t=p[1])
    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_lista_sentencias2(p):
    """lista_sentencias : empty"""
    p[0] = [p[1]]

def p_sentencia1(p):
    """sentencia : sentencia_expr """
    p[0] = p[1]

def p_sentencia2(p):
    """sentencia : sentencia_comp """
    p[0] = p[1]

def p_psentencia3(p):
    """sentencia : sentencia_seleccion """
    p[0] = p[1]

def p_sentencia4(p):
    """sentencia : sentencia_iteracion """
    p[0] = p[1]

def p_sentencia5(p):
    """sentencia : sentencia_retorno """
    p[0] = p[1]

def p_sentencia_expr1(p):
    """sentencia_expr : expresion PUNTOCOMA"""
    p[0] = p[1]

def p_sentencia_expr2(p):
    """sentencia_expr : PUNTOCOMA"""
    pass

def p_sentencia_seleccion1(p):
    """sentencia_seleccion : SI CORCHETEIZQ expresion CORCHETEDER sentencia"""
    p[0] = nodos.SentenciaSeleccion(p[1], p[2], p[3], p[4], p[5], None, None)

def p_sentencia_seleccion2(p):
    """sentencia_seleccion : SI CORCHETEIZQ expresion CORCHETEDER sentencia SINO sentencia """
    p[0] = nodos.SentenciaSeleccion(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_sentencia_iteracion1(p):
    """sentencia_iteracion : MIENTRAS CORCHETEIZQ expresion CORCHETEDER sentencia"""
    p[0] = nodos.SentenciaIteracion1(p[1], p[2], p[3], p[4], p[5])

def p_sentencia_iteracion2(p):
    """sentencia_iteracion : REP sentencia_comp"""
    p[0] = nodos.SentenciaIteracion2(p[1], p[2])

def p_sentencia_retorno1(p):
    """sentencia_retorno : RET PUNTOCOMA"""
    p[0] = p[1]

def p_sentencia_retorno2(p):
    """sentencia_retorno : RET expresion PUNTOCOMA"""
    p[0] = nodos.SentenciaRetorno(p[1], p[2])

def p_expresion1(p):
    """expresion : var IGUAL expresion"""
    p[0] = nodos.Expresion(p[1], p[3])

def p_expresion2(p):
    """expresion : expresion_negada"""
    p[0] = p[1]

def p_var1(p):
    """var : ID"""
    p[0] = p[1]

def p_var2(p):
    """var : ID LESSTHAN expresion GREATERTHAN"""
    p[0] = nodos.Var(p[1], p[2], p[3], p[4])

def p_expresion_negada1(p):
    """expresion_negada : NOT CORCHETEIZQ expresion_logica CORCHETEDER"""
    p[0] = nodos.ExpresionNegada(p[1], p[2], p[3], p[4])

def p_expresion_negada2(p):
    """expresion_negada : expresion_logica"""
    p[0] = p[1]

def p_expresion_logica1(p):
    """expresion_logica : expresion_logica AND expresion_simple"""
    p[0] = nodos.ExpresionLogica(p[1], p[2], None, None, p[3], None)

def p_expresion_logica2(p):
    """expresion_logica : expresion_logica AND NOT CORCHETEIZQ expresion_simple CORCHETEDER"""
    p[0] = nodos.ExpresionLogica(p[1], p[2], p[3], p[4], p[5], p[6])

def p_expresion_logica3(p):
    """expresion_logica : expresion_simple"""
    p[0] = p[1]

def p_expresion_logica4(p):
    """expresion_logica : NOT CORCHETEIZQ expresion_simple CORCHETEDER"""
    p[0] = nodos.ExpresionLogica(p[1], p[2], p[3], p[4], p[5], p[6])

def p_expresion_simple1(p):
    """expresion_simple : expresion_simple relop expresion_aditiva"""
    p[0] = nodos.ExpresionSimple(p[1], p[2], p[3])

def p_expresion_simple2(p):
    """expresion_simple : expresion_aditiva"""
    p[0] = p[1]

def p_relop1(p):
    """relop : LT """
    #pass
    p[0] = p[1]

def p_relop2(p):
    """relop : EQ"""
    p[0] = p[1]

def p_expresion_aditiva1(p):
    """expresion_aditiva : expresion_aditiva addop term"""
    p[0] = nodos.ExpresionAditiva(p[1], p[2], p[3])

def p_expresion_aditiva2(p):
    """expresion_aditiva : term"""
    p[0] = p[1]

def p_addop1(p):
    """addop : MAS"""
    p[0] = p[1]

def p_addop2(p):
    """addop : MENOS"""
    p[0] = p[1]

def p_term1(p):
    """term : term mulop factor"""
    p[0] = nodos.Term(p[1], p[2], p[3])

def p_term2(p):
    """term : factor"""
    p[0] = p[1]

def p_mulop1(p):
    """mulop : MASMAS"""
    p[0] = p[1]

def p_mulop2(p):
    """mulop : MENOSMENOS"""
    p[0] = p[1]

def p_factor1(p):
    """factor : CORCHETEIZQ expresion CORCHETEDER"""
    nodos.Factor(p[1], p[2], p[3])
    #p[0] = p[2]

def p_factor2(p):
    """factor : var"""
    p[0] = p[1]

def p_factor3(p):
    """factor : invocacion"""
    p[0] = p[1]

def p_factor4(p):
    """factor : NUM"""
    p[0] = p[1]

def p_invocacion(p):
    """invocacion : ID CORCHETEIZQ argumentos CORCHETEDER"""
    p[0] = nodos.Invocacion(p[1], p[2], p[3], p[4])

def p_argumentos1(p):
    """argumentos : lista_arg"""
    p[0] = p[1]

def p_argumentos2(p):
    """argumentos : empty"""
    pass

def p_lista_arg1(p):
    """lista_arg : lista_arg COMA expresion"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])


def p_lista_arg2(p):
    """lista_arg : expresion"""
    p[0] = p[1]


def p_empty(p):
    """empty : """
    pass

def p_error(p):
    print('Error de sintaxis! ')
    if p is not None:
        print('Error en el ' + str(p.type) + '\n')
    else:
        print('El archivo de entrada esta vacío\n')

# Build the parser
parser = yacc.yacc()


out = open('out1.dot', 'w')
with open('sample.txt', 'r') as arch:
    contents = arch.read()
    result = parser.parse(contents)
    if result is not None:
        visitor_tipos = Visitor()
        nodos.Programa.accept(result, visitor_tipos)
        out.write(visitor_tipos.ast)

        #llamado al tabla de simbolos visitor
        build_tabla_simbolos = BuildTablaSimbolosVisitor()
        nodos.Programa.accept2(result, build_tabla_simbolos)

    else:
        out.write('Error al realizar el parse.')