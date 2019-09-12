print("==== soma dos maiores ====")
x = int(input("digite um valor inteiro para x"))
y = int(input("digite um valor inteiro para y"))

if x > y:
    print(x - y)
elif y > x:
    print(y - x)
elif y == x:
    print("Os valores dados sao invalidos")
