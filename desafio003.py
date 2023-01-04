import random

def analisando_grelha(lista_de_grelhas):
    vegetarian = 0
    non_vegetarian =  0
    for grelha in lista_de_grelhas:
        if '-x' not in grelha and '-o' in grelha:
            vegetarian += 1
        elif '-x' in grelha:
            non_vegetarian += 1
    print(vegetarian, non_vegetarian)

    return vegetarian, non_vegetarian

def main():
    grelhas = ['---x--x--o-o--x--', '---x--x--x-x--x--', '--x-x----x--', '--o-----o--']
    analisando_grelha(grelhas)

if __name__ == '__main__':
    main()