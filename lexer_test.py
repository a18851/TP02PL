from lexer import ALexer
al = ALexer()
al.build()
al.input("F=10;")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")

