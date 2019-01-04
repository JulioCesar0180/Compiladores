from tabla_simbolos import *

class BuildTablaSimbolosVisitor(object):
    def __init__(self):
        self.ast = ''

    def visit_programa(self, programa):
        if programa.lista_decl1 is not None:
            if not isinstance(programa.lista_decl1, list):
                aux = [programa.lista_decl1]
            else:
                aux = programa.lista_decl1

            for stmt in aux:
                if stmt is not None:

                    stmt.accept2(self)


    def visit_declaracion_var(self, declaracion_var):

        funcion_global = NodoFuncionGlobales()

        if declaracion_var.NUM_t is not None:
            variable_global = nodoVariableGlobal(declaracion_var.def_tipo_p, declaracion_var.ID_t, True)
            NodoFuncionGlobales.agregarGlobal(funcion_global, variable_global)
        else:
            variable_global = nodoVariableGlobal(declaracion_var.def_tipo_p, declaracion_var.ID_t, False)
            NodoFuncionGlobales.agregarGlobal(funcion_global, variable_global)

        funcion_global.iterar()


    def visit_declaracion_fun(self, declaracion_fun):

        if declaracion_fun.parametros_p is not None:
            if isinstance(declaracion_fun.parametros_p, list):
                aux = declaracion_fun.parametros_p
            else:
                aux = [declaracion_fun.parametros_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    pass
                    #stmt.accept2(self)
        #declaracion_fun.sentencia_comp_p.accept2(self)

    def visit_param(self, param):

        if param.LESSTHAN_t is not None:
            pass

    def visit_sentencia_comp(self, sentencia_comp):

        if sentencia_comp.declaraciones_locales_p is not None:
            if isinstance(sentencia_comp.declaraciones_locales_p, list):
                aux = sentencia_comp.declaraciones_locales_p
            else:
                aux = [sentencia_comp.declaraciones_locales_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    stmt.accept2(self)

    def visit_declaraciones_locales(self, declaraciones_locales):

        if declaraciones_locales.declaraciones_locales_p is not None:
            if not isinstance(declaraciones_locales.declaraciones_locales_p, list):
                aux = [declaraciones_locales.declaraciones_locales_p]
            else:
                aux = declaraciones_locales.declaraciones_locales_p
            for stmt in aux:
                if stmt is not None:
                    stmt.accept2(self)

    def visit_sentencia_seleccion(self, sentencia_seleccion):

        if sentencia_seleccion.expresion_p is not None:
            if isinstance(sentencia_seleccion.expresion_p, list):
                aux = sentencia_seleccion.expresion_p
            else:
                aux = [sentencia_seleccion.expresion_p]
            for stmt in aux:
                if isinstance(stmt, str):
                   pass
                elif stmt is not None:
                    stmt.accept2(self)

        if sentencia_seleccion.sentencia1_p is not None:
            if isinstance(sentencia_seleccion.sentencia1_p, list):
                aux = sentencia_seleccion.sentencia1_p
            else:
                aux = [sentencia_seleccion.sentencia1_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    stmt.accept2(self)

        if sentencia_seleccion.SINO_t is not None:

            if sentencia_seleccion.sentencia2_p is not None:
                if isinstance(sentencia_seleccion.sentencia2_p, list):
                    aux = sentencia_seleccion.sentencia2_p
                else:
                    aux = [sentencia_seleccion.sentencia2_p]
                for stmt in aux:
                    if isinstance(stmt, str):
                        pass
                    elif stmt is not None:
                        stmt.accept2(self)

    def visit_expresion(self, expresion):

        pass


    def visit_var(self, var):

        if var.expresion1_p is not None:
            if not isinstance(var.expresion1_p, list):
                aux = [var.expresion1_p]
            else:
                aux = var.expresion1_p

            for stmt in aux:
                if stmt is not None:
                    stmt.accept2(self)

    def visit_expresion_negada(self, expresion_negada):

        if expresion_negada.expresion_logica_p is not None:
            if isinstance(expresion_negada.expresion_logica_p, list):
                aux = expresion_negada.expresion_logica_p
            else:
                aux = [expresion_negada.expresion_logica_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    stmt.accept2(self)

    def visit_sentencia_retorno(self, sentencia_retorno):
        pass

    def visit_sentencia_iteracion1(self, sentencia_iteracion):

        if sentencia_iteracion.expresion_p is not None:
            if not isinstance(sentencia_iteracion.expresion_p, list):
                aux = [sentencia_iteracion.expresion_p]
            else:
                aux = sentencia_iteracion.expresion_p

            for stmt in aux:
                if stmt is not None:
                    stmt.accept2(self)

        if sentencia_iteracion.sentencia_p is not None:
            if isinstance(sentencia_iteracion.sentencia_p, list):
                aux = sentencia_iteracion.sentencia_p
            else:
                aux = [sentencia_iteracion.sentencia_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    stmt.accept2(self)

    def visit_sentencia_iteracion2(self,sentencia_iteracion):

        if sentencia_iteracion.sentencia_comp_p is not None:
            if isinstance(sentencia_iteracion.sentencia_comp_p, list):
                aux = sentencia_iteracion.sentencia_comp_p
            else:
                aux = [sentencia_iteracion.sentencia_comp_p]
            for stmt in aux:
                if isinstance(stmt, str):
                    pass

                elif stmt is not None:
                    stmt.accept2(self)

    def visit_expresion_logica(self, expresion_logica):

        if expresion_logica.expresion_logica_p is not None:
            if isinstance(expresion_logica.expresion_logica_p, list):
                aux = expresion_logica.expresion_logica_p
            else:
                aux = [expresion_logica.expresion_logica_p]

            for stmt in aux:
                if isinstance(stmt, str):
                    pass

                elif stmt is not None:
                    stmt.accept2(self)

            if isinstance(expresion_logica.expresion_simple_p, list):
                aux = expresion_logica.expresion_simple_p
            else:
                aux = [expresion_logica.expresion_simple_p]

            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    stmt.accept2(self)
        else:

            if isinstance(expresion_logica.expresion_simple_p, list):
                aux = expresion_logica.expresion_simple_p
            else:
                aux = [expresion_logica.expresion_simple_p]

            for stmt in aux:
                if isinstance(stmt, str):
                    pass
                elif stmt is not None:
                    stmt.accept2(self)


    def visit_expresion_simple(self, expresion_simple):

        if expresion_simple.relop_p == 'EQ':
            pass
        else:
            pass

        if isinstance(expresion_simple.expresion_aditiva_p, list):
            aux = expresion_simple.expresion_aditiva_p
        else:
            aux = [expresion_simple.expresion_aditiva_p]

        for stmt in aux:
            if isinstance(stmt, str):
                pass
            elif stmt is not None:
                stmt.accept2(self)

    def visit_expresion_aditiva(self, expresion_aditiva):

        if expresion_aditiva.addop_p == '+':
            pass
        else:
            pass

        if isinstance(expresion_aditiva.term_p, list):
            aux = expresion_aditiva.term_p
        else:
            aux = [expresion_aditiva.term_p]

        for stmt in aux:
            if isinstance(stmt, str):
                pass
            elif stmt is not None:
                stmt.accept2(self)


    def visit_term(self, term):

        if term.mulop_p == '++':
            pass

        else:
            pass

        if isinstance(term.factor_p, list):
            aux = term.factor_p
        else:
            aux = [term.factor_p]

        for stmt in aux:
            if isinstance(stmt, str):
                pass
            elif stmt is not None:
                stmt.accept2(self)

    def visit_invocacion(self, invocacion):
        pass