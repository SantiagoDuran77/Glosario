# Ejercicio 1: Cálculo de áreas y elevación al cubo
# Área de un triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = base * altura / 2
print(f"El área del triángulo es: {area_triangulo}")

# Área de un cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))
area_cuadrado = lado * lado
print(f"El área del cuadrado es: {area_cuadrado}")

# Área de una circunferencia
import math
radio = float(input("Ingrese el radio de la circunferencia: "))
area_circunferencia = math.pi * radio**2
print(f"El área de la circunferencia es: {area_circunferencia}")

# Elevación al cubo
numero = float(input("Ingrese un número para elevar al cubo: "))
cubo = numero ** 3
print(f"El cubo de {numero} es: {cubo}")