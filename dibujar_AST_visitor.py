
class Visitor(object):
    def __init__(self):
        self.ast = ''
        self.id_nodo = 0
        self.id_programa = 0
        self.id_declaracion_var = 0
        self.id_declaracion_fun = 0
        self.id_param = 0
        self.id_lista_sentencias = 0
        self.id_sentencia_comp = 0
        self.id_declaraciones_locales = 0
        self.id_sentencia_seleccion = 0
        self.id_sentencia_iteracion1 = 0
        self.id_sentencia_iteracion2 = 0
        self.id_sentencia_retorno = 0
        self.id_expresion = 0
        self.id_var = 0
        self.id_expresion_negada = 0
        self.id_expresion_logica = 0
        self.id_expresion_logica2 = 0
        self.id_expresion_logica4 = 0
        self.id_expresion_simple = 0
        self.id_relop = 0
        self.id_expresion_aditiva = 0
        self.id_term = 0
        self.id_factor = 0
        self.id_invocacion = 0

#Para cada nodo, se le asigna un contador, esto con el fin de crear correctamente el árbol. De igual manera, por cada nodo creado, también tendrá un contador

    def visit_programa(self, programa):
        self.id_programa += 1
        id_programa = self.id_programa
        if programa.lista_decl1 is not None:
            if not isinstance(programa.lista_decl1, list):
                aux = [programa.lista_decl1]
            else:
                aux = programa.lista_decl1

            for stmt in aux:
                if stmt is not None:
                    self.ast += '\t"Programa ' + str(id_programa) + '" '
                    stmt.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'


#Se crea padre e hijo según corresponda, y se le asigna un número a cada nodo con el fin evitar problemas con los direccionamientos
    def visit_declaracion_var(self, declaracion_var):


        self.id_declaracion_var += 1
        id_declaracion_var = self.id_declaracion_var

        self.ast += ' -> "Declaracion_var ' + str(id_declaracion_var) + '"\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + declaracion_var.def_tipo_p + '"]\n'

        self.ast += '\t' + '"Declaracion_var ' + str(id_declaracion_var) + '" -> ' + str(self.id_nodo) + '\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + declaracion_var.ID_t + '"]\n'
        self.ast += '\t' + '"Declaracion_var ' + str(id_declaracion_var) + '" -> ' + str(self.id_nodo) + '\n'
        if declaracion_var.NUM_t is not None:
            self.id_nodo += 1
            self.ast += '\t' + str(self.id_nodo) + '[label="' + declaracion_var.NUM_t + '"]\n'
            self.ast += '\t' + '"Declaracion_var ' + str(id_declaracion_var) + '" -> ' + str(self.id_nodo) + '\n'


#Según lo mencionado anteriormente, cuando un camino contiene a otro, para simplificar nodos, se debe hacer lo siguiente"


    def visit_declaracion_fun(self, declaracion_fun):


        self.id_declaracion_fun += 1
        id_declaracion_fun = self.id_declaracion_fun

        self.ast += '-> "Declaracion_fun ' + str(id_declaracion_fun) + '"\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + declaracion_fun.def_tipo_p + '"]\n'
        self.ast += '\t"Declaracion_fun ' + str(id_declaracion_fun) + '" ->' + str(self.id_nodo) + '\n'

        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + declaracion_fun.ID_t + '"]\n'
        self.ast += '\t"Declaracion_fun ' + str(id_declaracion_fun) + '" ->' + str(self.id_nodo) + '\n'

        if declaracion_fun.parametros_p is not None:
            if isinstance(declaracion_fun.parametros_p, list):
                aux = declaracion_fun.parametros_p
            else:
                aux = [declaracion_fun.parametros_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Declaracion_fun ' + str(id_declaracion_fun) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Declaracion_fun ' + str(id_declaracion_fun) + '"\n'
                    stmt.accept(self)
        self.ast += '\t"Declaracion_fun ' + str(id_declaracion_fun) + '"\n'
        declaracion_fun.sentencia_comp_p.accept(self)


    def visit_param(self, param):

        self.id_param += 1
        id_param = self.id_param

        self.ast += '-> "Param ' + str(id_param) + '"\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + param.def_tipo_p + '"]\n'
        self.ast += '-> "Param ' + str(id_param) + '" -> ' + str(self.id_nodo) + '\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + param.ID_t + '"]\n'
        self.ast += '-> "Param ' + str(id_param) + '" -> ' + str(self.id_nodo) + '\n'

        if param.LESSTHAN_t is not None:
            self.id_nodo += 1
            self.ast += '\t' + str(self.id_nodo) + '[label="' + param.LESSTHAN_t + '"]\n'
            self.ast += '-> "Param ' + str(id_param) + '" -> ' + str(self.id_nodo) + '\n'
            self.id_nodo += 1
            self.ast += '\t' + str(self.id_nodo) + '[label="' + param.GREATERTHAN_t + '"]\n'
            self.ast += '-> "Param ' + str(id_param) + '" -> ' + str(self.id_nodo) + '\n'

    def visit_lista_sentencias(self, lista_sentencias):

        self.id_lista_sentencias += 1
        id_lista_sentencias = self.id_lista_sentencias

        if lista_sentencias.lista_sentencias1_p is not None:
            if not isinstance(lista_sentencias.lista_sentencias1_p, list):
                aux = [lista_sentencias.lista_sentencias1_p]
            else:
                aux = lista_sentencias.lista_sentencias1_p

            for stmt in aux:
                if stmt is not None:
                    stmt.accept(self)

        if lista_sentencias.sentencia_p is not None:
            if not isinstance(lista_sentencias.sentencia_p, list):
                aux = [lista_sentencias.sentencia_p]
            else:
                aux = lista_sentencias.sentencia_p

            for stmt in aux:
                if stmt is not None:
                    self.ast += '-> "Lista_Sentencias ' + str(id_lista_sentencias) + '"'
                    stmt.accept(self)

    def visit_sentencia_comp(self, sentencia_comp):


        self.id_sentencia_comp += 1
        id_sentencia_comp = self.id_sentencia_comp
        self.id_lista_sentencias += 1

        self.ast += '-> "Sentencia_Comp ' + str(id_sentencia_comp) + '"\n'

        if sentencia_comp.declaraciones_locales_p is not None:
            if isinstance(sentencia_comp.declaraciones_locales_p, list):
                aux = sentencia_comp.declaraciones_locales_p
            else:
                aux = [sentencia_comp.declaraciones_locales_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Sentencia_Comp ' + str(id_sentencia_comp) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Sentencia_Comp ' + str(id_sentencia_comp) + '"'
                    stmt.accept(self)

        if sentencia_comp.lista_sentencias1_p is not None:
            if isinstance(sentencia_comp.lista_sentencias1_p, list):
                aux = sentencia_comp.lista_sentencias1_p
            else:
                aux = [sentencia_comp.lista_sentencias1_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Sentencia_Comp ' + str(id_sentencia_comp) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Sentencia_Comp ' + str(id_sentencia_comp) + '"'
                    stmt.accept(self)


    def visit_declaraciones_locales(self, declaraciones_locales):
        self.id_declaraciones_locales += 1
        id_declaraciones_locales = self.id_declaraciones_locales


        if declaraciones_locales.declaraciones_locales_p is not None:
            if not isinstance(declaraciones_locales.declaraciones_locales_p, list):
                aux = [declaraciones_locales.declaraciones_locales_p]
            else:
                aux = declaraciones_locales.declaraciones_locales_p

            for stmt in aux:
                if stmt is not None:
                    self.ast += '-> "Tipo' + str(id_declaraciones_locales) + '"'
                    stmt.accept(self)

    def visit_sentencia_seleccion(self, sentencia_seleccion):



        self.id_sentencia_seleccion += 1
        id_sentencia_seleccion = self.id_sentencia_seleccion

        self.id_nodo += 1
        self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + sentencia_seleccion.SI_t + '"]\n'

        if sentencia_seleccion.expresion_p is not None:
            if isinstance(sentencia_seleccion.expresion_p, list):
                aux = sentencia_seleccion.expresion_p
            else:
                aux = [sentencia_seleccion.expresion_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '" ->' + str(self.id_nodo) + '\n'
                    self.ast += '\t"Lista_Sentencias 1' + '" ->' + '"Sentencia_Seleccion '+ str(id_sentencia_seleccion) + '"\n'
                elif stmt is not None:
                    self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '"'
                    stmt.accept(self)

        if sentencia_seleccion.sentencia1_p is not None:
            if isinstance(sentencia_seleccion.sentencia1_p, list):
                aux = sentencia_seleccion.sentencia1_p
            else:
                aux = [sentencia_seleccion.sentencia1_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '" ->' + str(
                        self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '"'
                    stmt.accept(self)

        if sentencia_seleccion.SINO_t is not None:

            self.id_nodo += 1
            self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '" ->' + str(self.id_nodo) + '\n'
            self.ast += '\t' + str(self.id_nodo) + '[label="' + sentencia_seleccion.SINO_t + '"]\n'

            if sentencia_seleccion.sentencia2_p is not None:
                if isinstance(sentencia_seleccion.sentencia2_p, list):
                    aux = sentencia_seleccion.sentencia2_p
                else:
                    aux = [sentencia_seleccion.sentencia2_p]
                for stmt in aux:
                    if isinstance(stmt, str):
                        self.id_nodo += 1
                        self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                        self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '" ->' + str(
                            self.id_nodo) + '\n'
                    elif stmt is not None:
                        self.ast += '\t"Sentencia_Seleccion ' + str(id_sentencia_seleccion) + '"'
                        stmt.accept(self)


    def visit_expresion(self, expresion):

        self.id_expresion += 1
        id_expresion = self.id_expresion


        self.ast += '-> "Expresion ' + str(id_expresion) + '"\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(expresion.var_p) + '"]\n'
        self.ast += '-> "Expresion ' + str(id_expresion) + '" -> ' + str(self.id_nodo) + '"\n'

        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + '=' + '"]\n'
        self.ast += '-> "Expresion ' + str(id_expresion) + '" -> ' + str(self.id_nodo) + '"\n'

        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(expresion.expresion1_p) + '"]\n'
        self.ast += '-> "Expresion ' + str(id_expresion) + '" -> ' + str(self.id_nodo) + '"\n'




    def visit_var(self, var):


        self.id_var += 1
        id_var = self.id_var

        self.ast += ' -> "Var ' + str(id_var) + '"\n'
        self.id_nodo += 1
        self.ast += '\t' + str(self.id_nodo) + '[label="' + var.ID_t + '"]\n'

        if var.expresion1_p is not None:
            if not isinstance(var.expresion1_p, list):
                aux = [var.expresion1_p]
            else:
                aux = var.expresion1_p

            for stmt in aux:
                if stmt is not None:
                    self.ast += '-> "Var ' + str(id_var) + '"'
                    stmt.accept(self)



    def visit_expresion_negada(self, expresion_negada):


        self.id_expresion_negada += 1
        id_expresion_negada = self.id_expresion_negada

        self.id_nodo += 1
        self.ast += '\t"Expresion_Negada ' + str(id_expresion_negada) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + expresion_negada.NOT_t + '"]\n'

        if expresion_negada.expresion_logica_p is not None:
            if isinstance(expresion_negada.expresion_logica_p, list):
                aux = expresion_negada.expresion_logica_p
            else:
                aux = [expresion_negada.expresion_logica_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Expresion_Negada ' + str(id_expresion_negada) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Expresion_Negada ' + str(id_expresion_negada) + '"'
                    stmt.accept(self)


    def visit_sentencia_retorno(self, sentencia_retorno):
        self.id_sentencia_retorno += 1
        id_sentencia_retorno = self.id_sentencia_retorno


        self.id_nodo += 1
        self.ast += '-> "Sentencia_retorno ' + str(id_sentencia_retorno) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(sentencia_retorno.expresion_p) + '"]\n'


    def visit_sentencia_iteracion1(self, sentencia_iteracion):
        self.id_sentencia_iteracion1 += 1
        id_sentencia_iteracion = self.id_sentencia_iteracion1

        self.id_nodo += 1
        self.ast += '-> "Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '"\n'

        self.id_nodo += 1
        self.ast += '\t"Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + sentencia_iteracion.MIENTRAS_t + '"]\n'

        if sentencia_iteracion.expresion_p is not None:
            if not isinstance(sentencia_iteracion.expresion_p, list):
                aux = [sentencia_iteracion.expresion_p]
            else:
                aux = sentencia_iteracion.expresion_p

            for stmt in aux:
                if stmt is not None:
                    self.ast += '-> "Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '"'
                    stmt.accept(self)



        if sentencia_iteracion.sentencia_p is not None:
            if isinstance(sentencia_iteracion.sentencia_p, list):
                aux = sentencia_iteracion.sentencia_p
            else:
                aux = [sentencia_iteracion.sentencia_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '->"Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '"'
                    stmt.accept(self)



    def visit_sentencia_iteracion2(self,sentencia_iteracion):
        self.id_sentencia_iteracion2 += 1
        id_sentencia_iteracion = self.id_sentencia_iteracion2

        self.id_nodo += 1
        self.ast += '-> "Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '"\n'

        self.id_nodo += 1
        self.ast += '\t"Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + sentencia_iteracion.REP_t + '"]\n'

        if sentencia_iteracion.sentencia_comp_p is not None:
            if isinstance(sentencia_iteracion.sentencia_comp_p, list):
                aux = sentencia_iteracion.sentencia_comp_p
            else:
                aux = [sentencia_iteracion.sentencia_comp_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '->"Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Sentencia_Iteracion ' + str(id_sentencia_iteracion) + '"'
                    stmt.accept(self)


    def visit_expresion_logica(self, expresion_logica):

        self.id_expresion_logica += 1
        id_expresion_logica = self.id_expresion_logica

        if expresion_logica.expresion_logica_p is not None:
            if isinstance(expresion_logica.expresion_logica_p, list):
                aux = expresion_logica.expresion_logica_p
            else:
                aux = [expresion_logica.expresion_logica_p]

            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Expresion_logica ' + str(id_expresion_logica) + '" ->' + str(self.id_nodo) + '\n'

                elif stmt is not None:
                    self.ast += '\t"Expresion_logica ' + str(id_expresion_logica) + '"'
                    stmt.accept(self)

            if isinstance(expresion_logica.expresion_simple_p, list):
                aux = expresion_logica.expresion_simple_p
            else:
                aux = [expresion_logica.expresion_simple_p]

            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Expresion_logica ' + str(id_expresion_logica) + '" ->' + str(self.id_nodo) + '\n'
                elif stmt is not None:
                    self.ast += '\t"Expresion_logica ' + str(id_expresion_logica) + '"'
                    stmt.accept(self)
        else:

            if isinstance(expresion_logica.expresion_simple_p, list):
                aux = expresion_logica.expresion_simple_p
            else:
                aux = [expresion_logica.expresion_simple_p]

            for stmt in aux:
                if isinstance(stmt, str):
                    self.id_nodo += 1
                    self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                    self.ast += '\t"Expresion_logica ' + str(id_expresion_logica) + '" ->' + str(self.id_nodo) + '\n'

                elif stmt is not None:
                    self.ast += '\t"Expresion_logica ' + str(id_expresion_logica) + '"'
                    stmt.accept(self)


    def visit_expresion_simple(self, expresion_simple):


        self.id_expresion_simple += 1
        id_expresion_simple = self.id_expresion_simple

        self.id_nodo += 1
        self.ast += ' -> "Expresion_simple ' + str(id_expresion_simple) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(expresion_simple.expresion_simple_p) + '"]\n'
        print(expresion_simple.expresion_simple_p)

        if expresion_simple.relop_p == 'EQ':
            self.id_nodo += 1
            self.ast += ' -> "Expresion_simple ' + str(id_expresion_simple) + '" ->' + str(self.id_nodo) + '\n'
            self.ast += '\t' + str(self.id_nodo) + '[label= "EQ"' + '"]\n'

        else:
            self.id_nodo += 1
            self.ast += ' -> "Expresion_simple ' + str(id_expresion_simple) + '" ->' + str(self.id_nodo) + '\n'
            self.ast += '\t' + str(self.id_nodo) + '[label= "LT"' + '"]\n'

        if isinstance(expresion_simple.expresion_aditiva_p, list):
            aux = expresion_simple.expresion_aditiva_p
        else:
            aux = [expresion_simple.expresion_aditiva_p]

        for stmt in aux:
            if isinstance(stmt, str):
                self.id_nodo += 1
                self.ast += ' -> "Expresion_simple ' + str(id_expresion_simple) + '" ->' + str(self.id_nodo) + '\n'
                self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
            elif stmt is not None:

                self.ast += ' -> "Expresion_simple ' + str(id_expresion_simple) + '" ->' + str(self.id_nodo) + '\n'
                stmt.accept(self)

    def visit_expresion_aditiva(self, expresion_aditiva):
        self.id_expresion_aditiva += 1
        id_expresion_aditiva = self.id_expresion_aditiva

        self.id_nodo += 1
        self.ast += ' -> "Expresion_aditiva ' + str(id_expresion_aditiva) + '" ->' + str(self.id_nodo) + '"\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(expresion_aditiva.expresion_aditiva_p) + '"]\n'


        if expresion_aditiva.addop_p == '+':
            self.id_nodo += 1
            self.ast += ' -> "Expresion_aditiva ' + str(id_expresion_aditiva) + '" ->' + str(self.id_nodo) + '"\n'
            self.ast += '\t' + str(self.id_nodo) + '[label="' + str(expresion_aditiva.addop_p) + '"]\n'

        else:
            self.id_nodo += 1
            self.ast += ' -> "Expresion_aditiva ' + str(id_expresion_aditiva) + '" ->' + str(self.id_nodo) + '"\n'
            self.ast += '\t' + str(self.id_nodo) + '[label= "-"' + ']\n'

        if isinstance(expresion_aditiva.term_p, list):
            aux = expresion_aditiva.term_p
        else:
            aux = [expresion_aditiva.term_p]

        for stmt in aux:
            if isinstance(stmt, str):
                self.id_nodo += 1
                self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                self.ast += '\t"Expresion_aditiva ' + str(id_expresion_aditiva) + '" ->' + str(self.id_nodo) + '\n'
            elif stmt is not None:
                self.ast += '\t"Expresion_aditiva ' + str(id_expresion_aditiva) + '"'
                stmt.accept(self)

    def visit_term(self, term):
        self.id_term += 1
        id_term = self.id_term

        self.id_nodo += 1
        self.ast += ' -> "Term ' + str(id_term) + '" ->' + str(self.id_nodo) + '\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(term.term_p) + '"]\n'

        if term.mulop_p == '++':
            self.id_nodo += 1
            self.ast += ' -> "Term ' + str(id_term) + '" ->' + str(self.id_nodo) + '\n'
            self.ast += '\t' + str(self.id_nodo) + '[label= "*"' + ']\n'

        else:
            self.id_nodo += 1
            self.ast += ' -> "Term ' + str(id_term) + '" ->' + str(self.id_nodo) + '\n'
            self.ast += '\t' + str(self.id_nodo) + '[label= "/"' + ']\n'

        if isinstance(term.factor_p, list):
            aux = term.factor_p
        else:
            aux = [term.factor_p]

        for stmt in aux:
            if isinstance(stmt, str):
                self.id_nodo += 1
                self.ast += '\t' + str(self.id_nodo) + '[label="' + stmt + '"]\n'
                self.ast += '\t"Term ' + str(id_term) + '" ->' + str(self.id_nodo) + '\n'
            elif stmt is not None:
                self.ast += '\t"Term ' + str(id_term) + '"'
                stmt.accept(self)


    def visit_invocacion(self, invocacion):
        self.id_invocacion += 1
        id_invocacion = self.id_invocacion

        self.id_nodo += 1
        self.ast += ' -> "Term ' + str(id_invocacion) + '" ->' + str(self.id_nodo) + '"\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(invocacion.ID_t) + '"]\n'

        self.id_nodo += 1
        self.ast += ' -> "Term ' + str(id_invocacion) + '" ->' + str(self.id_nodo) + '"\n'
        self.ast += '\t' + str(self.id_nodo) + '[label="' + str(invocacion.argumentos_p) + '"]\n'