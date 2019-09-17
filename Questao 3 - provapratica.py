print("==== Questao 3 ====")
base = int(input("Digite um valor inteiro para a base: "))
potenciaRaiz = int(input("Digite um valor inteiro para servir de raiz ou potencia: "))
tipoOperacao = (input("Agora informe se o que voce quer eh uma raiz ou potencia dos numeros que voce escolheu? Utilize 'pot' para potenciacao e 'rad' para radiciacao: " ))

if tipoOperacao == "pot":
    print("O resultado eh", base ** potenciaRaiz)
elif tipoOperacao == "rad":
    print("O resultado eh", base ** (1 / potenciaRaiz))