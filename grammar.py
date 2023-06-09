import ply.lex as lex
import ply.yacc as pyacc
import random
from lexer import ALexer

class AGrammar:

    precedence = (#("nonassoc", '>', '<'),   # level = 0
                    ("left", "+", '-'),     # level = 1 assoc = left interpretation = assoc left means (2+4)+6
                    ("left", '*'),
                    #("right", "minus")# level = 2 assoc = left interpretation = assoc on level 2 = 2+3*5 = 2+(3*5) or 2*3+6 = (2*3)+6
                  )
    # Definição da gramática
    def p_instrucao(self, p):
        '''
        instrucao : declaracao
                  | atribuicao
                  | escrita
                  | ENTRADA
                  | ALEATORIO
                  | ciclo
                  | comentario
        '''
        p[0] = p[1]

    def p_declaracao(self, p):
        'declaracao : VAR lista_variaveis'
        # Implementar a lógica para declarar as variáveis
        p[0] = p[2]

    def p_lista_variaveis(self, p):
        'lista_variaveis : IDENTIFICADOR'
        # Implementar a lógica para tratar uma lista de variáveis
        p[0] = p[1]

    def p_lista_variaveis_multiple(self, p):
        'lista_variaveis : lista_variaveis "," IDENTIFICADOR'
        # Implementar a lógica para tratar uma lista de variáveis separadas por vírgula
        p[0] = p[1] + ', ' + p[3]

    def p_atribuicao(self, p):
        'atribuicao : IDENTIFICADOR ATRIBUICAO expressao'
        # Implementar a lógica para atribuir um valor a uma variável
        p[0] = p[3]

    def p_atribuicao_leitura(self, p):
        'atribuicao : IDENTIFICADOR ATRIBUICAO ENTRADA'
        # Implementar a lógica para ler um valor do usuário e atribuir à variável
        p[0] = 'LER VALOR DO USUÁRIO'

    def p_atribuicao_aleatorio(self, p):
        'atribuicao : IDENTIFICADOR ATRIBUICAO ALEATORIO'
        # Implementar a lógica para gerar um valor aleatório e atribuir à variável
        p[0] = 'GERAR VALOR ALEATÓRIO'

    def p_expressao(self, p):
        '''
        expressao : NUMERO
                  | STRING
                  | IDENTIFICADOR
                  | expressao '+' expressao
                  | expressao '-' expressao
                  | expressao '*' expressao
                  | expressao '/' expressao
        '''
        # Implementar a lógica para avaliar uma expressão aritmética
        p[0] = p[1]

    def p_escrita(self, p):
        ' escrita : ESCREVER STRING '
        # Implementar a lógica para imprimir os argumentos na tela
        p[0] = p[2]

    def p_lista_argumentos(self, p):
        'lista_argumentos : argumento'
        # Implementar a lógica para tratar uma lista de argumentos
        p[0] = p[1]

    def p_lista_argumentos_multiple(self, p):
        'lista_argumentos : lista_argumentos argumento'
        # Implementar a lógica para tratar uma lista de argumentos separados por vírgula
        p[0] = p[1] + ', ' + p[2]

    def p_argumento(self, p):
        '''
        argumento : expressao
                  | STRING
        '''
        p[0] = p[1]

    def p_ciclo(self, p):
        'ciclo : PARA IDENTIFICADOR EM "[" NUMERO ELIPSIS NUMERO "]" FAZER instrucao FIM'
        # Implementar a lógica para executar um loop
        p[0] = 'LOOP'

    def p_comentario(self, p):
        '''
        comentario : COMENTARIO
                   | COMENTARIO_MULTILINHA
        '''
        p[0] = 'COMENTÁRIO'

    # Lidar com erros de sintaxe
    def p_error(self, p):
        print(f'Sintaxe inválida: {p.value}')


    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = ALexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)



