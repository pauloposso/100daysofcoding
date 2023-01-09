def sock_pairs(string):
    qtd_pares = 0
    if string != '':
        base_comparacao = set(list(string))
        for item in base_comparacao:
            contagem = round((string.count(item)-0.4)/2)
            qtd_pares += contagem
    else:
        print('A gavete parece estar vazia...')

    return qtd_pares

def main():
    pares =  'AABBAACCCCAABC'
    print(sock_pairs(pares))
    vazia = ''
    print(sock_pairs(vazia))


if __name__ == '__main__':
    main()