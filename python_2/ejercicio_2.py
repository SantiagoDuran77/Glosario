# Ejercicio 2: Calcular el interés simple por meses
capital = float(input("Ingrese el capital: "))
tasa = float(input("Ingrese la tasa de interés anual (%): "))
tiempo = float(input("Ingrese el tiempo (meses): "))
interes = (capital * (tasa / 12) * tiempo) / 100
print(f"El interés simple es: {interes}")