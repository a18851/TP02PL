# arith.py
from grammar import AGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = AGrammar()
ag.build()
string = "ola mundo"

#NAO LE PARENTESES BEM
exemplos = [# exemplos a avaliar de forma independente...
            "E=10;",
            "F=10; G=3*-5+7;",   #"3*-5+7"  3*(-5)+7
            "G=3*F; H=G*2;",
            "I=-2; J=I*-2; K=I+1;",
            "PARA x EM [ 10 ... 20 ] FAZER , FIM;"
            ]
for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    res = ag.parse ( frase )
    print("resultado: ")
    pp.pprint(res)
