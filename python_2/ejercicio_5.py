# Ejercicio 5 Calcular la edad de un paciente
from datetime import datetime

fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

fecha_actual = datetime.now()

edad = fecha_actual.year - fecha_nacimiento.year
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

print(f"La edad del paciente es: {edad} años")