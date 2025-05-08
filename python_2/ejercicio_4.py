# Ejercicio 4: Calcular el promedio de sueldos de un empleado durante un año
print("Ingrese los sueldos mensuales del empleado durante un año:")
sueldos = []
for mes in range(1, 13):
    sueldo = float(input(f"Sueldo del mes {mes}: "))
    sueldos.append(sueldo)
promedio = sum(sueldos) / len(sueldos)
print(f"El promedio de sueldos del empleado durante el año es: {promedio}")