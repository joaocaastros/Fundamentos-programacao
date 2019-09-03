print("==== CONVERSOR DE TEMPERATURA ====")
temperatura = float(input("Quantos graus de temperatura esta medindo no momento?"))
unidade = input("Qual a unidade de temperatura voce esta utilizando? Utilize C para graus celsius e F para graus farenheit")
if unidade == "C":
     print("A temperatura, em graus farenheit, eh", temperatura * 1.8 + 32,  "°F")
elif unidade == "F":
    print("A temperatura, em graus celsius, eh", (temperatura - 32) / 1.8, "°C" )
else:
    print("Voce digitou a unidade errada, SEU BURRO, JUMENTO, CORNO E ENGANADO!")
       