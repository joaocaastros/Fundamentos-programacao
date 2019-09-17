print("==== Questao 4 ====")
angulo1 = int(input("Informe um primeiro valor de angulo para o triangulo: "))
angulo2 = int(input("Informe um segundo valor de angulo para o triangulo: "))
angulo3 = int(input("Informe um segundo valor de angulo para o triangulo: "))

soma = (angulo1 + angulo2 + angulo3)
if soma == 180 and angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Os valores dos angulos correspondem a um triangulo, e o mesmo eh retangulo")
elif soma == 180 and angulo1 != 90 or angulo2 != 90 or angulo3 != 90:
    print("Eh um triangulo, porem nao eh retangulo")