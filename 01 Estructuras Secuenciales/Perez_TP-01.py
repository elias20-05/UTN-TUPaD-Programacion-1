#ejericcio1

print("Hola Mundo!")

#Ejercicio2

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#Ejercicio3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese su residencia: ")
print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio4

import math
radio_del_circulo = int(input("Ingrese el radio del circulo: "))
valor_pi = math.pi
area_del_circulo = round(math.pi * (radio_del_circulo**2),2)
perimetro_del_circulo = round(2 * math.pi * radio_del_circulo,2)
print(f"El Area del circulo es: {area_del_circulo}")
print(f"El Perimetro del circulo es: {perimetro_del_circulo}")

#Ejercicio5

segundos = float(input("Ingrese los segundos que quiera: "))
horas = round(segundos / 3600,2)
print(f"Los segundo ingresados {segundos} pasados a horas equivale a {horas}")

#Ejercicio6

numero = int(input("Mostrando la tabla del numero que ingrese: "))
print(f"{numero} x 1 = {1*numero}")
print(f"{numero} x 2 = {2*numero}")
print(f"{numero} x 3 = {3*numero}")
print(f"{numero} x 4 = {4*numero}")
print(f"{numero} x 5 = {5*numero}")
print(f"{numero} x 6 = {6*numero}")
print(f"{numero} x 7 = {7*numero}")
print(f"{numero} x 8 = {8*numero}")
print(f"{numero} x 9 = {9*numero}")
print(f"{numero} x 10 = {10*numero}")

#Ejercicio7

numero_1 = int(input("ingrese el primer numero, Distinto de 0: "))
numero_2 = int(input("ingrese el segundo numero, Distinto de 0: "))
print(f"Suma: {numero_1 + numero_2}")
print(f"Division: {numero_1 / numero_2}")
print(f"Multiplicacion: {numero_1 * numero_2}")
print(f"Resta: {numero_1 - numero_2}")

#Ejercicio8

altura = float(input("Ingrese su altura: "))
peso = float(input("ingrese su peso: "))
indice_masa_corporal = round(peso / (altura**2),1)
print(f"Sabiendo que pesas {peso}kg y medis {altura} de altura, tu indice de masa corporal es: {indice_masa_corporal}")

#Ejercicio9

temperatura_celsius =float(input("ingrese una temperatua en celsius: "))
temperatura_fahrenheit= round((temperatura_celsius*9/5) + 32)
print(f"La temperatura {temperatura_celsius} en fahrenheit es: {temperatura_fahrenheit} grados" )

#Ejercicio10

numero_1 = float(input("ingrese el primer numero: "))
numero_2 = float(input("ingrese el segundo numero: "))
numero_3 = float(input("ingrese el tercer numero: "))
promedio = (numero_1 + numero_2 + numero_3)/3
print(f"El promedio de los tres numeros es: {promedio}")