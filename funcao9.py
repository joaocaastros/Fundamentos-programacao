print("==== CALCULO DO AUMENTO SALARIAL ====")

def reajustar(salarioAtual):
    novoSalario = salarioAtual + salarioAtual * 0.15
    return novoSalario

salario = float(input("Qual o valor do seu salario?"))
salarioReajustado = reajustar(salario)

print("o valor do seu salario reajustado em 15% eh:", salarioReajustado)