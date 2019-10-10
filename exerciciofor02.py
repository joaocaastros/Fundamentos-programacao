import math

menor = math.inf
maior = - math.inf 

for i in range(10):
    numero = int(input("Digite um valor inteiro, por favor: "))


    if( numero > maior ):
        maior = numero
    if (numero < menor):
        menor = numero


print("O maior eh ", maior)
print("O menor eh ", menor)    