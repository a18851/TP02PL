from lexer import ALexer
al = ALexer()
al.build()
al.input("PARA x EM [ 10 ... 20 ] FAZER , FIM PARA;")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")

