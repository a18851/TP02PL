from lexer import ALexer
al = ALexer()
al.build()
al.input("x = 1 + x")  # "(3+5)*7")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")

