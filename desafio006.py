def try_if_prime(numero):
    primo = True
    for num in range(2, numero):
        x = numero/num
        if x - int(x) == 0:
            primo = False
            break
        else:
            pass
    
    return primo

def next_prime(numero):
    prox_primo = False
    while prox_primo == False:
        prox_primo = try_if_prime(numero+1)
        numero += 1
    
    return numero

def main():
    testar_prox_primo = input("Digite um número e eu te retorno o próximo número primo depois dele: ")
    try:
        testar_prox_primo = int(testar_prox_primo)
    except:
        print('Parece que vc não digitou um número inteiro...')
    teste = next_prime(testar_prox_primo)
    print(teste)

if __name__ == '__main__':
    main()