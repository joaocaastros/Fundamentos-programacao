# controle processual
# ------> usuario define quando para

controle = ""
estado = ""

while (controle != "X"):
    print("Houve evolucao no processo?")
    controle = input("Digite [S] para sim, [N] para não e [X] para sair: ")

    if (controle == "S"):
        estado = input("Qual o novo estado? ")
        print("o estado atual do processo eh:", estado)
    elif (controle == "N"):
        print(":( OK")
    print("")
if (controle == "X"):
    print("Processo sem movimentacao")
