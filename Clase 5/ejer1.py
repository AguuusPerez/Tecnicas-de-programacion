# CLASE 5

# Escribir un programa que pregunte el nombre del usuario en la consola
# y un numero entero, e imprima por pantalla en lineas distintas
# el nombre del usuario tantas veces como el numero introducido. 

nombre = input("Ingrese su nombre:")
cantidad = int(input("Ingrese cantidad:"))

# Validar que ingrese numeros positivos 
while cantidad < 0:
    print("Ingreso nro no valido, Solo se aceptan nros POSITIVOS")
    cantidad = int(input("Ingrese cantidad:"))

               
i = 0
while i < cantidad:
    print(nombre)
    i = i + 1             
    
    