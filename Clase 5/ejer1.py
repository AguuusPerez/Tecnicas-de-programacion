# Clase 5 - Ejercitacion while 
"""Escribir un programa que pregunte el nombre del usuario en la consola y un numero entero 
e imprima por pantalla en lineas distintas el nombre del usuario tantas veces como el numero introducido. """

nombre = input("Ingrese un nombre: ")
cantidad = int(input("Ingrese un numero entero: "))

# Validar que ingrese numeros positivos 
while cantidad < 0:
    print("Ingresaste un numero NO VALIDO")
    cantidad = int(input("Ingrese un numero entero: "))

i = 0    
while i < cantidad:
    print(nombre)
    i = i + 1         # incrementador 
    


