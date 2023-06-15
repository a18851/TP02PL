from grammar import AGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = AGrammar()
ag.build()
string = " ESCREVER x;"

# List of examples to evaluate
exemplos = [
    "E=10;",
    "F=10; G=3*-5+7;",   #"3*-5+7"  3*(-5)+7
    "G=3*(5+7); H=G*2;",
    "I=-2; J=I*-2; G=I+1;",
    string,
    "VAR x;"
]

for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    res = ag.parse(frase)
    print("resultado: ")
    pp.pprint(res)