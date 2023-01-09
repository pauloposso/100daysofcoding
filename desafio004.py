def progress_days(lista_distancias_percorridas):
    if lista_distancias_percorridas != []:
        base = lista_distancias_percorridas[0]
        contador = 0
        for distancia in lista_distancias_percorridas:
            if distancia > base:
                contador += 1
                base = distancia
            else:
                base = distancia
        print(f'Para esta lista de treinos Johnny teve {contador} dias de progresso.')
    else:
        print('Favor informar a as distâncias percorridas por Johnny.')

    return contador

def main():
    lista_treinos = []
    for x in range(1, 11):
        dia = input(f'Informe a distancia percorrida por Johnny no dia {x}: ')
        try:
            dia = int(dia)
        except ValueError:
            print('A distância percorrida por Johnny deve ser um número inteiro...')
        lista_treinos.append(dia)
    print(f'A lista de treinos de Johnny ficou dessa forma {lista_treinos}')
    dias_de_progresso = progress_days(lista_treinos)

if __name__ == '__main__':
    main()