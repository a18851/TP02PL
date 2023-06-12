import ply.lex as plex

class ALexer:

    # Definição dos tokens
    tokens = (
        'VAR',
        'NUMERO',
        'STRING',
        'IDENTIFICADOR',
        'ATRIBUICAO',
        'PARA',
        'FAZER',
        'FIM',
        'ESCREVER',
        'ENTRADA',
        'ALEATORIO',
        'COMENTARIO',
        'ELIPSIS',
        'EM',
        'COMENTARIO_MULTILINHA'
    )

    literals =";()+-*/[]^%:.{},"
    t_ignore = "\t "


    # Expressões regulares para os tokens

    def t_VAR(self, t):
        r'VARS'
        return t

    def t_ESCREVER(self, t):
        r'ESCREVER|escrever|esc|ESC'
        return t

    def t_NUMERO(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    def t_IDENTIFICADOR(self, t):
        r'[a-zA-Z]+'
        return t

    def t_ATRIBUICAO(self, t):
        r'='
        return t

    def t_STRING(self, t):
        r"""\'[A-Za-z]+[0-9]*\'"""
        t.value = t.value[1:-1]  # Remover as aspas
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

    def t_ENTRADA(self, t):
        r'ENTRADA\(\)|entrada\(\)'
        return t

    def t_ALEATORIO(self, t):
        r'ALEATORIO\(\d+\)|aleatorio\(\d+\)'
        return t

    def t_ELIPSIS(self, t):
        r'\.\.\.'
        return t

    def t_EM(self, t):
        r'EM|em'
        return t

    def t_COMENTARIO(self, t):
        r'//.*|\/\*(.|\n)*?\*\/'
        return t

    def t_COMENTARIO_MULTILINHA(self, t):
        r'\r//.*|\/\*(.|\n)*?\*\/'
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









































