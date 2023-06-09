from lexer import ALexer
al = ALexer()
al.build()
al.input("x = 44545 + x")  # "(3+5)*7")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")

