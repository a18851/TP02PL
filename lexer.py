import ply.lex as plex

class ALexer:

    # Definição dos tokens
    tokens = (
        'ID',
        'VAR',
        'V',
        'CARACTER',
        'REAL',
        'INTEIRO',
        'STRING',
        'ATRIBUICAO',
        'PARA',
        'FAZER',
        'FIM',
        'EM',
        'SE',
        'SENAO',
        'ENTAO',
        'FIM_SE',
        'FUNCAO',
        'FIM_FUNCAO',
        'NOT',
        'ESCREVER',
        'ELIPSIS',
        'DEFINITION_INTEIRO',
        'DEFINITION_REAL',
        'DEFINITION_CARACTER',
        'DEFENITION_LOGICO',
        'AND',
        'OR',
        'XOR',
        'TRUE',
        'FALSE',
        'NOT_EQUAL',
        'EQUAL',
        'BIGGER',
        'BIGGER_EQUAL',
        'SMALLER',
        'SMALLER_EQUAL'
    )

    literals =";()+-*/[]^%:.{},"
    t_ignore = "\t\n "


    # Expressões regulares para os tokens

    def t_V(self, t):
        r'VAR'
        return t

    def t_DEFINITION_INTEIRO(self, t):
        r"""inteiro"""
        return t

    def t_DEFINITION_REAL(self, t):
        r"""real"""
        return t

    def t_DEFINITION_CARACTER(self, t):
        r"""caracter"""
        return t

    def t_DEFENITION_LOGICO(self, t):
        r"""logico"""
        return t

    def t_AND(self, t):
        """and"""
        t.type = "and"
        return t

    def t_OR(self, t):
        """or"""
        t.type = "or"
        return t

    def t_XOR(self, t):
        """xor"""
        t.type = "xor"
        return t

    def t_ELIPSIS(self, t):
        r'\.\.\.'
        return t

    def t_EM(self, t):
        r'EM|em'
        return t

    def t_SE(self, t):
        r'SE|se'
        return t

    def t_SENAO(self, t):
        r'SENAO|senao'
        return t

    def t_ENTAO(self, t):
        r'ENTAO|entao'
        return t

    def t_FIM_SE(self, t):
        r'FIM_SE|fim_se'
        return t

    def t_FUNCAO(self, t):
        r'funcao|FUNCAO'
        return t

    def t_FIM_FUNCAO(self, t):
        r'FIM_FUNCAO|fim_funcao'
        return t

    def t_NOT(self, t):
        r'NOT|not'
        return t

    def t_ENQUANTO(self, t):
        r'ENQUANTO|enquanto'
        return t

    def t_PARA(self, t):
        r'PARA|para'
        return t

    def t_FAZER(self, t):
        r'FAZER|fazer'
        return t

    def t_FIM(self, t):
        r'FIM|fim'
        return t

    def t_ESCREVER(self, t):
        r'ESCREVER|escrever|esc|ESC'
        return t

    def t_CARACTER(self, t):
        r'"[^"]*"'
        t.type = "caracter"
        t.value = t.value[1:-1]
        return t

    def t_STRING(self, t):
        r'"([^"\\]|\\.)*"'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_REAL(self, t):
        r"""\d+\.\d+"""
        t.value = float(t.value)
        return t

    def t_INTEIRO(self, t):
        r"""\d+"""
        t.value = int(t.value)
        return t

    def t_ATRIBUICAO(self, t):
        r'='
        return t

    def t_EQUAL(self, t):
        r"""=="""
        return t

    def t_NOT_EQUAL(self, t):
        r"""!="""
        return t

    def t_TRUE(self, t):
        r"""(true)|(True)"""
        t.value = bool(t.value)
        t.type = "true"
        return t

    def t_FALSE(self, t):
        r"""(false)|(False)"""
        t.value = bool(t.value)
        t.type = "false"
        return t

    def t_SMALLER(self, t):
        r"""<|(<=)"""
        if t.value == "<=":
            t.type = "smaller_equal"
        else:
            t.type = "smaller"
        return t

    def t_BIGGER(self, t):
        r""">|(>=)"""
        if t.value == ">=":
            t.type = "bigger_equal"
        else:
            t.type = "bigger_equal"
        return t

    def t_VAR(self, t):
        r"""[a-z_]+[0-9]*"""
        t.type = "var"
        return t

    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        token = self.lexer.token()
        return token.type if token is not None else None

    def t_error(self, t):
        print("Token inesperado: [{}]".format(t.value[:10]))
        exit(1)
