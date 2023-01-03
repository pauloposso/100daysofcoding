def find_nemo(texto):
    try:
        achei = texto.split(' ').index('Nemo')
        print(f'Encontrei Nemo na posição {achei+1}')
    except ValueError:
        print('Não localizei Nemo...')

def main():
    frase = input('Insira uma frase para que eu procure Nemo: ')
    find_nemo(frase)

if __name__ == '__main__':
    main()