from lexer import ALexer
al = ALexer()
al.build()
al.input("PARA x EM [ 10 ... 20 ] FAZER x = x + 1 FIM PARA;")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")

