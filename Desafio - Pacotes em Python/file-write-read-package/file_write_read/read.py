try:
    arquivo = input('Informe o nome do arquivo (.txt): ')

    with open(arquivo, 'r') as arq:
        print(arq.read())

except FileNotFoundError:
    print('Arquivo não encontrado.')