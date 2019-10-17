tinto = 0
rose = 0
branco = 0

vinhos = [ "[1] tinto ", "[2] rose ", "[3] branco"]

for i in range(10):
    print("Através dos códigos, escolha o seu vinho, sendo [1] para tinto, [2] para rose e [3] para branco: ")

    for tipo in vinhos:
        print(tipo)
    

    escolha = input()

if(escolha == "1"):
    tinto += 1
elif(escolha == "2"):
    rose += 1
elif(escolha == "3"):
    branco += 1
else:
    print("opcao invalida")

print("Tinto", tinto )
print("Branco", branco)
print("Rose", rose) 