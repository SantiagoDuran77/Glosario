# Ejercicio 3: Conversor de dolar a peso y viceversa
tasa_dolar_a_peso = float(input("Tasa de dolar a peso: "))
tasa_peso_a_dolar = 1 / tasa_dolar_a_peso

dolar = float(input("Cantidad en dolares: "))
pesos = dolar * tasa_dolar_a_peso
print("Equivalente en pesos:", pesos)

pesos = float(input("Cantidad en pesos: "))
dolar = pesos / tasa_dolar_a_peso 
print("Equivalente en dolares:", dolar)