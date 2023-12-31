try:
    arquivo = open('emails.txt')
except FileNotFoundError:
    print('Arquivo não existe')


