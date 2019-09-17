print("==== Questao 1 =====")
salarioRenda = float(input("Informe o valor de sua renda mensal somando todos os seus ganhos/salario: "))

if salarioRenda <= 1800:
    print ("Voce esta na encaixado na faixa salarial 1 do Programa Minha Casa Minha Vida, portanto, esta isento de juros - taxa 0%")
elif salarioRenda >= 1801 and salarioRenda <= 2600:
    print("Voce esta encaixado na faixa salarial 1,5 do Programa Minha Casa Minha Vida, portanto, sua taxa de juros eh de 5%")
elif salarioRenda >= 2601 and salarioRenda <= 3000:
    print("Voce esta encaixado na faixa salarial 2 do Programa Minha Casa Minha Vida e sua taxa de juros eh 6%")
elif salarioRenda >= 3001 and salarioRenda <= 4000:
    print("Voce esta encaixado na faixa salarial 2 do Programa Minha Casa Minha Vida, e sua taxa de juros eh 7%")
elif salarioRenda >= 4001 and salarioRenda <= 7000:
    print("Voce esta encaixado na faixa salarial 3 do Programa Minha Casa Minha Vida, e sua taxa de juros eh 8,16%")
elif salarioRenda >= 7001 and salarioRenda <= 9000:
    print("Voce esta encaixado na faixa salarial 3 do Programa Minha Casa Minha Vida, e sua taxa de juros eh 9,16%")