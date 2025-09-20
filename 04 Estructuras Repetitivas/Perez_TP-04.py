#Ejercicio 1

for x in range(0,100):
    print(x)

#Ejercicio 2

import math 
#ingreso de datos
numeroInt = int(input("Ingrese un numero entero: "))
#asignandole a la variable "digitos" , math.log10,(para poder encontrar la cantidad de digitos del numero ingresado)
digitos = int(math.log10(numeroInt)) + 1
#finalmente mostramos la cantidad de digitos
print(f"El numero que ingreso tiene {digitos} digitos")

#Ejercicio 3

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))
suma = 0
for x in range(numero1+1,numero2, +1):
    suma = suma + x
    
print(f"La suma es: {suma}")

#Ejercicio 4

import random
print("tiene que adivinar el numero entre el 0 y el 9 ")
intentos = 0
numero = int(input("ingrese el numero: "))
numero_azar = random.randint(0,9)
while numero_azar != 0:
    if numero == numero_azar:
        print("lo isiste")
        break
    else:
        intentos = intentos+1
        break
print(numero_azar)


#Ejercicio 5

import random
print("tienes que adivinar el numero aleatorio entre el 0 y el 9 ")
intentos = 0

numero_azar = random.randint(0,9)
while numero_azar != 0:
    numero = int(input("ingrese el numero: "))
    intentos += 1
    if numero == numero_azar:
        print("lo isiste")
        break
    
print(f"Necesitaste {intentos} intentos para acertar el numero")
    

#Ejercicio 6


primos = 0
for num in range(100, -1, -2):
    primos = num
    print(primos)
    


#Ejercicio 7

suma = 0
numero = int(input("ingrese un numero: "))
for x in range(0,numero):
    suma = suma + x

print(f"La suma de todos los numero hasta el numero ingresado {suma}")


#Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0

cantidad_numeros = int(input("ingrese la cantidad de numeros: "))

# Solicitar números al usuario
for i in range(cantidad_numeros):
    try:
        num = int(input(f"Ingrese el número {i+1}: "))
        
        # Contar pares e impares
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        # Contar positivos y negativos
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
            
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        i -= 1  # Decrementar para repetir la iteración

# Mostrar resultados
print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
    
#Ejercicio 9

cantidad_numeros = 5
suma = 0
media_numeros = 0

for i in range(cantidad_numeros):
        num = float(input(f"Ingrese el número {i+1}: "))
        
        suma = suma + num
        media_numeros =  suma/cantidad_numeros

# Mostrar resultados
print("\nResultado:")
print(f"La media de los numeros ingresados es: {media_numeros}")

    
#Ejercicio 10

numero = int(input("Ingrese un número entero: "))

es_negativo = numero < 0
numero = abs(numero)

numero_invertido = int(str(numero)[::-1])

if es_negativo:
    numero_invertido = -numero_invertido

print(f"El número con dígitos invertidos es: {numero_invertido}")
    
    