def conversor_idade_em_dias(idade):
    total_dias = int(idade) * 365
    print(f'Convertendo sua idade em dias, você viveu {total_dias} até hoje...')

    return total_dias

def main():
    idade = input('Insira sua idade: ')
    conversor_idade_em_dias(idade)

if __name__ == '__main__':
    main()