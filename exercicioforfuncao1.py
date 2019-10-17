def somaQuadradosImpares(inteiros) :
    total = 0
    for valor in inteiros:
        if(valor != 0) :
            total = total + valor ** 2
    
    return total 

numeros1 = [10, 20, 30, 40]
numeros2 = [11, 22, 33, 44]
numeros3 = [13, 15, 16, 18]
numeros4 = [41, 45, 46, 50, 100, 202, 34, 56, 78, 75, 12, 137, 242, 245, 30, 18]

total1 = somaQuadradosImpares(numeros1)
total2 = somaQuadradosImpares(numeros2)
total3 = somaQuadradosImpares(numeros3)
total4 = somaQuadradosImpares(numeros4)

print(total1)
print(total2)
print(total3)
print(total4)

