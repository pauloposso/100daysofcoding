from itertools import product

def fazendo_combinacoes():
    teclado = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

    preenchido = False
    while not preenchido:
        digits = input('Insira uma sequencia de até 4 dígitos entro 2-9 para que eu possa fazer as possíveis combinações: ')
        if 0 > len(digits) > 4:
            print("Você deve digitar até 4 números...")
        elif 2222 >= int(digits) >= 9999:
            print('Se atente, você pode escolher até 4 números de 2 a 9...')
        else:
            try: 
                lista1 = teclado[digits[0]]
            except:
                lista1 = [None]
            try: 
                lista2 = teclado[digits[1]]
            except:
                lista2 = [None]
            try: 
                lista3 = teclado[digits[2]]
            except:
                lista3 = [None]
            try: 
                lista4 = teclado[digits[3]]
            except:
                lista4 = [None]
            # result = list(product(lista1, lista2, lista3, lista4))
            combinacoes = []
            for a in lista1:
                for b in lista2:
                    for c in lista3:
                            for d in lista4:
                                result = [a, b, c, d]
                                combinacoes.append(result)
            for lista in combinacoes:
                lista.remove(None)
            preenchido = True
            
            return combinacoes


    
def main():
   combinacoes = fazendo_combinacoes()
   print(combinacoes)

if __name__ == '__main__':
    main()