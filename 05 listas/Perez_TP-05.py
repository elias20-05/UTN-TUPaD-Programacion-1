#Ejercicio(1)

lista =  [i*4 for i in range(0,26 ) if i < 100 ]

print(lista)

#Ejercicio(2)

#forma de hacer (1)

lista1 = [12,45,11,87]
cantidad = len(lista1)
penultimo1 = lista1[2]
print(f"El penultimo numero de la lista {lista1} es: {penultimo1}")

#forma de hacer (2)

lista2 = [11,34,67,98,78]
penultimo2 = lista2[-2]
print(f"El penultimo numero de la lista {lista2} es: {penultimo2}")

#Ejercicio(3)


lista_vacia = []

lista_vacia.append(["hola","mundo","mañana"])
con_tres_palabras = lista_vacia
print(con_tres_palabras)

#Ejercicio(4)


animales = ["perro", "gato", "conejo", "pez"]

animales[3] = "oso"
animales[1] = "loro"

print(animales)

#Ejercicio(5)

#Analizar el siguiente programa y explicar con tus palabras que es lo que realiza
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#ANALISIS:
#En la primera line se realiza una lista llamada "numero" la cual contiene 5 numeros [8,15,3,22,7].
#En la segunda linea veo que se usa "remove", la cual sirve para eliminar un elemento de la lista, se utiliza con "max" para buscar el numero mayor de la lista y luego lo elimina.
#y al final se muestra la lista sin el numero mayor de la lista.

#Ejercicio(6)

lista = [i for i in range(10,31,5)]
print(lista)
print([lista[0],lista[1]])

#Ejercicio(7)

autos = ["sedan", "polo", "suran", "gol"]
autos[1],autos[2] = "fiat","renault"

print(autos)


#Ejercicio(8)

dobles = []
dobles.append([10,20,30])
print(dobles)


#Ejercicio(9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
eliminar = "pan"
for i in compras:
    if eliminar in i:
        i.remove(eliminar)

print(compras)

#Ejercicio(10)


lista_anidada = [[15],[True],[[25.5],[57.9],[30.6]],[False]]
print(lista_anidada)
