def contarConsoantes(texto):
    totalDeConsoantes = 0
    
    for letra in texto:
        if (letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u"):
            totalDeConsoantes = totalDeConsoantes + 1
    print(totalDeConsoantes)

palavra = input("Digite uma palavra: ")
contarConsoantes(palavra)
