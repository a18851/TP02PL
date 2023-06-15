# Função para interpretar o arquivo de entrada ou comandos do terminal
from lexer import ALexer
from grammar import AGrammar
from eval import AEval
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

lg = AGrammar()
lg.build()

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            ast_tree = lg.parse(contents)
            pp.pprint(ast_tree)
            AEval.evaluate(ast_tree)
        except Exception as e:
            print(e, file=sys.stderr)
else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ast = lg.parse(expr)
            pp.pprint(ast)
            res = AEval.evaluate(ast)
            #if res is not None:
            print(f"<< {res}")

        except Exception as e:
            print(e)

