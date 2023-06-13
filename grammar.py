import ply.yacc as pyacc
from lexer import ALexer

class AGrammar:

#    precedence = (#("nonassoc", '>', '<'),   # level = 0
#                    ("left", "+", '-'),     # level = 1 assoc = left interpretation = assoc left means (2+4)+6
#                    ("left", '*'),
#                    #("right", "minus")# level = 2 assoc = left interpretation = assoc on level 2 = 2+3*5 = 2+(3*5) or 2*3+6 = (2*3)+6
#                  )
#    # Definição da gramática
#    def p_instrucao(self, p):
#        '''
#        instrucao : declaracao
#                  | atribuicao
#                  | escrita
#                  | ENTRADA
#                  | ALEATORIO
#                  | ciclo
#                  | comentario
#        '''
#        p[0] = p[1]
#
#    def p_declaracao(self, p):
#        'declaracao : VAR lista_variaveis'
#        # Implementar a lógica para declarar as variáveis
#        p[0] = p[2]
#
#    def p_lista_variaveis(self, p):
#        'lista_variaveis : IDENTIFICADOR'
#        # Implementar a lógica para tratar uma lista de variáveis
#        p[0] = p[1]
#
#    def p_lista_variaveis_multiple(self, p):
#        'lista_variaveis : lista_variaveis "," IDENTIFICADOR'
#        # Implementar a lógica para tratar uma lista de variáveis separadas por vírgula
#        p[0] = p[1] + ', ' + p[3]
#
#    def p_atribuicao(self, p):
#        'atribuicao : IDENTIFICADOR ATRIBUICAO expressao'
#        # Implementar a lógica para atribuir um valor a uma variável
#        p[0] = p[3]
#
#    def p_atribuicao_leitura(self, p):
#        'atribuicao : IDENTIFICADOR ATRIBUICAO ENTRADA'
#        # Implementar a lógica para ler um valor do usuário e atribuir à variável
#        p[0] = 'LER VALOR DO USUÁRIO'
#
#    def p_atribuicao_aleatorio(self, p):
#        'atribuicao : IDENTIFICADOR ATRIBUICAO ALEATORIO'
#        # Implementar a lógica para gerar um valor aleatório e atribuir à variável
#        p[0] = 'GERAR VALOR ALEATÓRIO'
#
#    def p_expressao(self, p):
#        '''
#        expressao : NUMERO
#                  | STRING
#                  | IDENTIFICADOR
#                  | expressao '+' expressao
#                  | expressao '-' expressao
#                  | expressao '*' expressao
#                  | expressao '/' expressao
#        '''
#        # Implementar a lógica para avaliar uma expressão aritmética
#        p[0] = p[1]
#
#    def p_escrita(self, p):
#        ' escrita : ESCREVER STRING '
#        # Implementar a lógica para imprimir os argumentos na tela
#        p[0] = p[2]
#
##    def p_lista_argumentos(self, p):
##        'lista_argumentos : argumento'
##        # Implementar a lógica para tratar uma lista de argumentos
##        p[0] = p[1]
##
##    def p_lista_argumentos_multiple(self, p):
##        'lista_argumentos : lista_argumentos argumento'
##        # Implementar a lógica para tratar uma lista de argumentos separados por vírgula
##        p[0] = p[1] + ', ' + p[2]
##
##    def p_argumento(self, p):
##        '''
##        argumento : expressao
##                  | STRING
##        '''
##        p[0] = p[1]
#
#    def p_ciclo(self, p):
#        'ciclo : PARA IDENTIFICADOR EM "[" NUMERO ELIPSIS NUMERO "]" FAZER instrucao FIM'
#        # Implementar a lógica para executar um loop
#        p[0] = 'LOOP'
#
#    def p_comentario(self, p):
#        '''
#        comentario : COMENTARIO
#                   | COMENTARIO_MULTILINHA
#        '''
#        p[0] = 'COMENTÁRIO'
#
#    # Lidar com erros de sintax
#    def p_error(self, p):
#        if p:
#            print(f"Syntax error: unexpected '{p.type}'")
#        else:
#            print("Syntax error: unexpected end of file")
#        exit(1)

    precedence = (
        ('left', '+', '-'),
        ('left', '*'),
        ('right', 'simetrico'),
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

    def p_s(self, p):
        """S : LstV ';'"""
        p[0] = p[1]

    def p_expr_tail(self, p):
        """LstV : LstV ';' Inst"""
        lstArgs = p[1]['args']
        lstArgs.append(p[3])
        p[0] = dict(op='seq', args=lstArgs)

    def p_expr_head(self, p):
        """LstV : Inst"""
        p[0] = dict(op='seq', args=[p[1]])

    def p_expr_inst_atr(self, p):
        """Inst : V"""
        p[0] = p[1]

    def p_expr_inst_esc(self, p):
        """Inst : ESCREVER E
                | ESCREVER STRING
                | ESCREVER NUMERO """
        p[0] = {'op': 'esc', 'args': [p[2]]}

    def p_expr_inst_esc2(self, p):
        """ Inst : ESCREVER E ',' Inst
                 | ESCREVER STRING ',' Inst
                 | ESCREVER NUMERO ',' Inst"""
        p[0] = {'op': 'esc', 'args': [p[2]]}

    def p_expr_atrib(self, p):
        """V : IDENTIFICADOR ATRIBUICAO E
             | IDENTIFICADOR ATRIBUICAO STRING """
        variable_name = p[1]
        self.variables[variable_name] = p[3]
        p[0] = dict(op='atr', args=[variable_name, p[3]])

    def p_expr_atrib2(self, p):
        """V : VAR IDENTIFICADOR ATRIBUICAO E
             | VAR IDENTIFICADOR ATRIBUICAO E ',' V"""
        variable_name = p[2]
        self.variables[variable_name] = p[4]
        p[0] = dict(op='atr', args=[variable_name, p[4]])

    def p_expr_op(self, p):
        """E : E '+' E
             | E '-' E
             | E '*' E
             | E ':' E"""
        p[0] = dict(op=p[2], args=[p[1], p[3]])

    def p_expr_sinalmenos(self, p):
        """E : '-' E %prec simetrico"""
        p[0] = dict(op='-', args=[p[2]])

    def p_expr_pare(self, p):
        """E : '(' E ')'"""
        p[0] = p[2]

    def p_expr_num(self, p):
        """E : NUMERO"""
        p[0] = p[1]

    def p_expr_var(self, p):
        """E : IDENTIFICADOR"""
        variable_name = p[1]
        if variable_name not in self.variables:
            print(f"Error: Variable '{variable_name}' not declared.")
            exit(1)
        p[0] = {'var': variable_name}

        def p_ciclo(self, p):
            'ciclo : PARA IDENTIFICADOR EM "[" NUMERO ELIPSIS NUMERO "]" FAZER lista_instrucoes FIM PARA'
            p[0] = {'tipo': 'ciclo', 'variavel': p[2], 'inicio': p[5], 'fim': p[7], 'instrucoes': p[10]}

        def p_lista_instrucoes(self, p):
            '''
            lista_instrucoes : instrucao
                             | instrucao lista_instrucoes
            '''
            if len(p) == 2:
                p[0] = [p[1]]
            else:
                p[0] = [p[1]] + p[2]

            def p_escrita_multiple(self, p):
                '''escrita : escrita ',' STRING'''
                p[0] = p[1] + ', ' + p[3]

            def p_escrita_single(self, p):
                '''escrita : ESCREVER STRING'''
                p[0] = p[2]

def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)

