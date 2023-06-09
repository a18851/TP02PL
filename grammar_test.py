# arith.py
from grammar import AGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = AGrammar()
ag.build()

exemplos = [ # exemplos a avaliar de forma independente...
            "E=10;",
            "F=10; G=3*-5+7;"  #"3*-5+7"  3*(-5)+7
            ]
for frase in exemplos:
    print("----------------------")
    print("--- frase '{}'".format(frase))
    res = ag.parse(frase)
    print("resultado: ")
    pp.pprint(res)
