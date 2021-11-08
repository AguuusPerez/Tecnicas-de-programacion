# Clase 5 - Ejercitacion while 
# Leer numeros enteros positivios de teclado, hasta que el usuario ingrese el 0. 
# Informar cual fue el mayor ingresado 
menor = 999999
mayor = -1  
numero = int(input("Ingrese un numero: "))

while numero > 0:
    if numero > mayor:
        mayor = numero 
    if numero < menor:
        menor = numero 
    numero = int(input("Ingrese un numero:  "))
    
print("Mayor numero ingresado: {} - Menor numero ingresado: {}" .format(mayor, menor))