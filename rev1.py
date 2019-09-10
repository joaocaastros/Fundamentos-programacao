print("==== Formula de Baskara =====")
a = float(input("digite o valor de a"))
b = float(input("digite o valor de b"))
c = float(input("digite o valor de c"))

#calcula o valor do delta
delta = b**2 - 4 * a * c

#calcula o valor do x quando delta eh positivo
x1 = (-b + delta ** (1/2) / 2*a)

#calcula o valor do x quando delta eh negativo
x2 = (-b - delta ** (1/2) / 2*a)

print("Os valores possiveis de x sao", x1, "e", x2)