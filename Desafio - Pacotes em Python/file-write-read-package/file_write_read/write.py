from datetime import datetime

arquivo = input('Informe o nome do arquivo (.txt): ')

if '.txt' in arquivo:
    with open(arquivo, 'a') as arq:
        mensagem = input('Digite a mensagem que deseja escrever:\n')
        arq.write(f'{mensagem}\nCriação: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n')
else:
    print('Tipo de arquivo incorreto. Informe um arquivo do tipo (.txt)')