print("==== Calculo salarial ====")
horas = float(input("Informe quantidade de horas trabalhadas: "))
precohora = float(input("Qual o valor da hora de trabalho? "))
descontoIR = float(input("Digite o valor, em porcentagem, deduzido pela receita do seu salario "))

salariobruto = (horas * precohora)
salarioliquido = salariobruto - salariobruto * descontoIR / 100
if salarioliquido < 1000:
    print("Esse eh seu salario", salarioliquido, "seu LISO")
elif salarioliquido >= 1000 and salarioliquido < 3000:
    print("Pobretao vey, mas ate que", salarioliquido, "ta bom, vai...")
elif salarioliquido >= 3000 and salarioliquido < 5000:
    print("Razoavel, razoavel... se liga:", salarioliquido)
elif salarioliquido >=  5000 and salarioliquido < 10000 :
    print("Ta enrycando, neh? Se liga na grana:", salarioliquido)
elif salarioliquido >= 10000:
    print("Burgues opressor... ganhando", salarioliquido, "faz doacao pros pobres, seu bolsominion!")