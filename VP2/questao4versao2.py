def contarConsoantes(texto):
    totalDeConsoantes = 0
    
    for letra in texto:
        if letra not in "aeiou":
            totalDeConsoantes = totalDeConsoantes + 1
    print(totalDeConsoantes)

palavra = input("Digite uma palavra: ")
contarConsoantes(palavra)
