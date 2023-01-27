import math

def bst_combinations(n):
    c = math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
    print(int(c))
   
def main():
    n = input("Digite um número de 1 a 19: ")
    try:
        n = int(n)
    except:
        print("Você deve digitar um número...")
    if 0 > n > 19:
        print('Tem que ser um número entre 1 e 19')
    else:
        bst_combinations(n)

if __name__ == '__main__':
    main()