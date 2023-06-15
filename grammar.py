import ply.yacc as pyacc
from lexer import ALexer

class AGrammar:

    precedence = (
        ("left", "OR", "XOR"),  # lower priority
        ("left", "AND"),
        ("left", "BIGGER"),
        ("left", "BIGGER_EQUAL"),
        ("left", "SMALLER"),
        ("left", "SMALLER_EQUAL"),
        ("left", "EQUAL"),
        ("left", "NOT_EQUAL"),
        ("left", "+", "-"),
        ("left", "*", "/"),
        ("right", "uminus"),  # higher priority - numeros negativos
    )

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None
        self.variables = {}  # Dicionário para armazenar as variáveis e seus valores

    def build(self, **kwargs):
        self.lexer = ALexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_code1(self, p):
        """ code : com_list """
        p[0] = [p[1]]

    def p_com_list(self, p):
        """ com_list : command
                    | com_list command """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]]
            p[0].append(p[2])

    def p_command1(self, p):
        """ command : e ';'
                    | ciclo_for
                    | callfunc ';'
                    | if
                    | func """
        p[0] = p[1]

    def p_command2(self, p):
        """ command : VARS VAR ATRIBUICAO var_list ';' """
        variable_name = p[2]
        self.variables[variable_name] = p[4]
        p[0] = dict(op='atr', args=[variable_name, p[4]])

    def p_command3(self, p):
        """ command : ESCREVER var_list
                    | ESCREVER e_list """
        p[0] = {'op': 'esc', 'args': [p[2]]}

    def p_ciclo_for(self, p):
        """ ciclo_for : PARA VARS EM "[" INTEIRO ELIPSIS INTEIRO "]" FAZER com_list FIM """
        p[0] = {'tipo': 'ciclo', 'variavel': p[2], 'inicio': p[5], 'fim': p[7], 'instrucoes': p[10]}

        if len(p) == 12:
            p[0] = {
                "op": "for",
                "args": [p[2], p[4], p[6], p[8]],
                "data": [p[10]]

            }
        else:
            p[0] = {
                "op": "for",
                "args": [p[2], p[4], p[6]],
                "data": [p[8]],
            }


    def p_if(self, p):
        """ if : SE e ENTAO com_list FIM_SE
                | SE e ENTAO com_list SENAO com_list FIM_SE """
        if len(p) == 6:
            p[0] = {
                "op": "if",
                "args": [p[2]],
                "data": [p[4]]
                }
        else:
            p[0] = {
                "op": "if",
                "args": [p[2]],
                "data": [p[4], p[6]]
            }

    def p_func(self, p):
        """ func : FUNCAO VAR '(' var_fun_list ')' com_list FIM_FUNCAO
                 | FUNCAO VAR '(' ')' com_list FIM_FUNCAO """
        if len(p) == 8:
            p[0] = {
                "op": "func",
                "args": [],
                "data": [p[2], p[4], p[6]]
            }
        else:
            p[0] = {
                "op": "func",
                "args": [],
                "data": [p[2], [], p[6]]
            }

    def p_callfunc(self, p):
        """ callfunc : VAR '(' e_list ')'
                     | VAR '(' ')'  """
        p[0] = {"op": "call",
                "args": [],
                "data": [p[1], [] if p[3] == ')' else p[3]]}

    def p_var_fun_list(self, p):
        """ var_fun_list : var_fun
                         | var_fun_list ',' var_fun """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_var_fun(self, p):
        """ var_fun : type VAR """
        if len(p) == 3:
            p[0] = {"var": p[2], "type": p[1], "scope": "local"}

    def p_var_list(self, p):
        """ var_list : VAR
                     | var_list ',' VAR """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_e_list(self, p):
        """ e_list : e
                   | e_list ',' e """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_e1(self, p):
        """ e : REAL
              | INTEIRO
              | CARACTER
              | condicao
              | '-' e  %prec uminus  """
        p[0] = p[1] if len(p) == 2 else {"op": "-", "args": [0, p[2]]}

    def p_e2(self, p):
        """ e : e '*' e
              | e '/' e
              | e '+' e
              | e '-' e """
        p[0] = dict(op=p[2], args=[p[1], p[3]])

    def p_e3(self, p):
        """ e : logico
              | e OR e
              | e AND e
              | e XOR e """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = dict(op=p[2], args=[p[1], p[3]])

    def p_e4(self, p):
        """ e : '(' e ')' """
        p[0] = p[2]

    def p_e5(self, p):
        """ e : VAR """
        p[0] = {"var": p[1]}

    def p_condicao(self, p):
        """ condicao : e SMALLER e
                     | e SMALLER_EQUAL e
                     | e BIGGER e
                     | e BIGGER_EQUAL e
                     | e EQUAL e
                     | e NOT_EQUAL e """
        p[0] = dict(op=p[2], args=[p[1], p[3]])

    def p_type(self, p):
        """ type : DEFINITION_INTEIRO
                 | DEFINITION_REAL
                 | DEFINITION_CARACTER
                 | DEFENITION_LOGICO """
        p[0] = p[1]

    def p_l1(self, p):
        """ logico : TRUE """
        p[0] = True

    def p_l2(self, p):
        """ logico : FALSE """
        p[0] = False

    def p_l3(self, p):
        """ logico : NOT logico """
        p[0] = dict(op="not", args=[p[2]])

    def p_error(self, p):
        if p:
            raise Exception(f"Parse Error: Unexpected token '{p.type}' line '{p.lineno}'")
        else:
            raise Exception("Parse Error: Expecting token")


