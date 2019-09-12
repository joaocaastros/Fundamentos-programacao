print("==== Calculo da soma dos quadrados ====")
x = int(input("digite um primeiro valor "))
y = int(input("digite um segundo valor "))
z = int(input("digite um terceiro valor "))

if (x < y): 
    if (y < z):
        print(x, y, z)
    else:
        if (x < z):
            print(x, z, y)
        else:
            print(z, x, y)
else:
    if (y < z):
        if (x < z):
            print(y, x, z)
        else:
            print(y, z, x)
    else:
        print(z, y, x)                           