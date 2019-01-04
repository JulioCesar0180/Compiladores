from ply import lex
#import re
import io

"""
 Se declaran todos los tokens a utilizar
"""
tokens = ['SINO',
          'SI',
          'ENT',
          'VACUO',
          'RET',
          'MIENTRAS',
          'REP',
          'MASMAS',
          'MAS',
          'MENOSMENOS',
          'MENOS',
          'LT',
          'EQ',
          'AND',
          'NOT',
          'IGUAL',
          'CORCHETEDER',
          'CORCHETEIZQ',
          'LESSTHAN',
          'GREATERTHAN',
          'PARENTESISDER',
          'PARENTESISIZQ',
          'COMA',
          'PUNTOCOMA',
          'ID',
          'NUM'
          ]

"""
 Para las Palabras Claves y Reservadas, se deben colocar antes que todo lo demás, y especificar explícitamente
 su "palabra". Dado que son case sensitive, deben incluir (?!)
"""

"""
 Para SINO
"""
def t_SINO(t):
    r'(?i)sino'
    return t

"""
 Para SI
"""
def t_SI(t):
    r'(?i)si'
    return t

"""
 Para ent
"""
def t_ENT(t):
    r'(?i)ent'
    return t

"""
 Para vacuo
"""
def t_VACUO(t):
    r'(?i)vacuo'
    return t

"""
 Para ret
"""
def t_RET(t):
    r'(?i)ret'
    return t

"""
 Para mientras
"""
def t_MIENTRAS(t):
    r'(?i)mientras'
    return t

"""
 Para rep
"""
def t_REP(t):
    r'(?i)rep'
    return t

"""
 Desde acá, se va separar lo mas posible para cada caso, y no abarcar todo en una misma sección
"""

"""
 Para el ++
"""
def t_MASMAS(t):
    r'\+\+'
    return t

"""
 Para el +
"""
def t_MAS(t):
    r'\+'
    return t

"""
 Para el --
"""
def t_MENOSMENOS(t):
    r'--'
    return t

"""
 Para el -
"""
def t_MENOS(t):
    r'-'
    return t

"""
 Para LT
"""
def t_LT(t):
    r'(?i)LT'
    return t

"""
 Para EQ
"""
def t_EQ(t):
    r'(?i)EQ'
    return t

"""
 Para &&
"""
def t_AND(t):
    r'&&'
    return t

"""
 Para !
"""
def t_NOT(t):
    r'!'
    return t

"""
 Para =
"""
def t_IGUAL(t):
    r'='
    return t

"""
 Para ]
"""
def t_CORCHETEDER(t):
    r'\]'
    return t

"""
 Para [
"""
def t_CORCHETEIZQ(t):
    r'\['
    return t

"""
 Para <
"""
def t_LESSTHAN(t):
    r'<'
    return t

"""
 Para >
"""
def t_GREATERTHAN(t):
    r'>'
    return t

"""
 Para )
"""
def t_PARENTESISDER(t):
    r'\)'
    return t

"""
 Para (
"""
def t_PARENTESISIZQ(t):
    r'\('
    return t

"""
 Para ,
"""
def t_COMA(t):
    r','
    return t

"""
 Para ;
"""
def t_PUNTOCOMA(t):
    r';'
    return t

"""
 Debe comenzar con minúsculas: [a-z]
 Debe ser case sensitive y cualquier cantidad de letras: {a-zA-Z]*
 Para que no existan $ consecutivas, si se opta por poner un $, se debe colocar cualquir cantidad de letras despues: (\$[A-Za-z]+)
 Dado que es opcional todo lo mencionado anteriormente, se le coloca un ?
 Para asegurar que no existan $ consecutivos antes de los numeros, se coloca ? además que es opcional colocarlo.
 Finalmente, se termina colocando cualquier cantidad de numeros, y es opcional: [0-9] 
"""
def t_ID(t):
    r'[a-z]([A-Za-z]*(\$[A-Za-z]+)*)?(\$)?[0-9]*'
    return t

"""
 Para hexadecimal: Dado que puede estar desde el 0 al 9, y las letras son de a hasta f en minuscula, en cualquier posicion, se utiliza: [0-9a-f]+ y luego el sufijo "#16"
 Para decimal:  Simplemente es [0-9]+
 Para Octal: Debe colocarse [0-9]+ acompañado del sufijo "#8"
"""
def t_NUM(t):
    r'([0-9a-f]+\#16)|([0-7]+\#8)|([0-9]+)'
    return t

"""
 Los comentarios de una linea se pueden usar de dos formas, la primera forma es anteponer # seguido de
 cualquier texto, simbolo o numero. La segunda forma es anteponer */ seguido de 
 cualquier texto, simbolo o numero y terminar con /*.
"""
def t_COMENTARIOS(t):
    r'((\#).*)'
    pass

"""
 El comentario multi linea consiste en anteponer */ seguido de cualquier texto, 
 simbolo o numero y terminar con /*. Esta puede tener saltos de linea
"""
def t_COMENTARIOMULTI(t):
    r'\*/([^/\*]|[\r\n])*/\*'
    pass

t_ignore = ' \t\n'  # Ignorar esto!

def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    # Tratamiento de errores.
    t.lexer.skip(1)

lexer = lex.lex()

out = open('out1.dot', 'w')
with open('sample.txt', 'r') as f:
    contents = f.read()
    lex.input(contents)
    for tok in iter(lex.token, None):
        print (repr(tok.type), repr(tok.value))