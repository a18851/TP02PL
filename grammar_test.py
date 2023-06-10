# arith.py
from grammar import AGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = AGrammar()
ag.build()


#NAO LE PARENTESES BEM
exemplos = [# exemplos a avaliar de forma independente...
            "E=10;",
            "F=10; G=3*-5+7;",   #"3*-5+7"  3*(-5)+7
            "G=3*(5+7); H=G*2;",
            "I=-2; J=I*-2; K=I+1;",
            "ESCREVER X+1;"
            ]
for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    res = ag.parse ( frase )
    print("resultado: ")
    pp.pprint(res)
