opcao = input("Você quer mnúmeros pares ou ímpares? ")

if (opcao == "pares") :
    # corpo do 
    for i in range (0, 200):
        if (i % 2 == 0):
            print(1)
elif (opcao == "impares"):
    #corpo do elif
    for i in range (0, 201):
        if (i % 2 != 0):
            print (i)
else:
    # corpo do else
    print("Opcao invalida")