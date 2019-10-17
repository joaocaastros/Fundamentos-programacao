def ehPalindromo(texto) :
    textoAoContrario = ""

    for letra in texto:
        textoAoContrario = letra + textoAoContrario

    if texto == textoAoContrario:
        return True
    else:
        return False

print(ehPalindromo("exercicio"))