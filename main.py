# Função para interpretar o arquivo de entrada ou comandos do terminal
from grammar import AGrammar

ag = AGrammar()
ag.build()

def interpretar_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        entrada = f.read()
        resultado = ag.parse(entrada)
        print(resultado)


def interpretar_terminal():
    while True:
        entrada = input('>>> ')
        if entrada == 'sair':
            break
        resultado = ag.parse(entrada)
        print(resultado)

# Exemplo de uso
if __name__ == '__main__':
    interpretar_arquivo('ex.ea')
    # Ou
    interpretar_terminal()


# Função principal
def main():
    nome_arquivo = "ex.ea"
    interpretar_arquivo(nome_arquivo)

if __name__ == '__main__':
    main()
