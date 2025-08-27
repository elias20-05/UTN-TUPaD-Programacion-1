#Ejercicio(1) 

#ingreso de datos del usuario
edad_usuario = int(input("ingrese su edad: "))
#si la edad ingresada es mayor a 18 se mostrara el mansaje"Es mayor de edad"
if edad_usuario > 18:
    print("Es mayor de edad")
    
#Ejercicio(2)

#ingreso de datos del usuario
nota_del_usuario = float(input("ingrese su nota , por favor: "))
if nota_del_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
#Ejercicio(3)

numero_par = int(input("ingrese un numero par: "))

if numero_par % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("por favor, ingrese un numero par")
    
#Ejercicio(4)

#ingreso de la edad del usuario
edad_del_usuario = int(input("Por favor, ingrese su edad: "))
if edad_del_usuario >= 30:
    print("CATEGORIA: Adulto/a")
elif edad_del_usuario >= 18 and edad_del_usuario < 30:
    print("CATEGORIA: Adulto/a Joven")
elif edad_del_usuario >= 12 and edad_del_usuario < 18:
    print("CATEGORIA: Adolecente")
else:
    print("CATEGORIA: Niño/a")

#Ejercicio(5)

contraseña = input("ingrese una contrseña de 8 a 14 caracteres: ")
caracteres_contraseña = len(contraseña)
if caracteres_contraseña >= 8 and caracteres_contraseña <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de 8 a 14 caracteres")

#Ejercicio(6)

import random
from statistics import mean, median, mode

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
mean(numeros_aleatorios)
median(numeros_aleatorios)
mode(numeros_aleatorios)
    
# Comparar para determinar el sesgo
if mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo o a la izquierda")
elif mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo o a la derecha")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")
else:
    print("No se cumple ninguna condición clara de sesgo")

print(mean(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mode(numeros_aleatorios))

#Ejercicio(7)

# Solicitar una frase o palabra al usuario
frase_o_palabra = input("Ingrese una frase o palabra: ")

# Definir las vocales (mayúsculas y minúsculas)
vocales = "aeiouAEIOU"

# Verificar si el último carácter es una vocal
if frase_o_palabra and  frase_o_palabra[-1] in vocales:
    resultado = frase_o_palabra + "!"
else:
    resultado = frase_o_palabra

# Imprimir el resultado
print(resultado)

#Ejercicio(8)
#Solicitar el nombre y la opcion
nombre = input("ingrese su nombre: ")
print("Seleccione la opcion que desee")
print("opcion (1):Si quiere su nombre en mayúsculas.")
print("opcion (2):Si quiere su nombre en minúsculas.")
print("opcion (3):Si quiere su nombre con la primera letra mayúscula.")
opciones = int(input("Seleccion: "))

# Transformar el nombre según la opción seleccionada
if opciones == 1:
    nombre = nombre.upper()
    print(nombre)
elif opciones == 2:
    nombre = nombre.lower()
    print(nombre)
elif opciones == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print(nombre)# En caso de que la opción sea inválida, se mantiene el nombre original

#Ejercicio(9)

#Solicitar al usuario la magnitud de un terremoto
magnitud_del_terremoto = float(input("ingrese la magnitud de un terremoto: "))
#Evaluar la magnitud y clasificarla segun la escala de intensidad
if magnitud_del_terremoto < 3:
    print("Muy Leve (imperceptible)")
elif magnitud_del_terremoto >= 3 and magnitud_del_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_del_terremoto >= 4 and magnitud_del_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_del_terremoto >= 5 and magnitud_del_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_del_terremoto >= 6 and magnitud_del_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_del_terremoto >= 7 :
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio(10)

# Solicitar hemisferio, mes y día
hemisferio = input("Ingrese hemisferio (N o S): ").upper()
mes = int(input("Ingrese mes (1-12): "))
dia = int(input("Ingrese día (1-31): "))

# Determinar la estación según la tabla
if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == 'N':
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == 'N':
        print("Primavera")
    else:
        print("Otoño")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == 'N':
        print("Verano")
    else:
        print("Invierno")
else:
    if hemisferio == 'N':
        print("Otoño")
    else:
        print("Primavera")