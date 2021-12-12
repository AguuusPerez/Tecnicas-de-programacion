# CLASE 5 

# Leer numeros enteros positivos de teclado, hasta que el usuario ingrese 0
# Informar cual fue el mayor numero ingresado
 

numero = int(input("Ingrese numero: "))
mayor = -1
menor = 99999

while numero > 0:
    if numero > mayor:
        mayor = numero
    if numero < menor:   #numero menor ingresado
        menor = numero
        
    numero = int(input("Ingrese numero: "))    
    
print("Mayor numero ingresado: {}".format(mayor))   
print("Menor numero ingresado: {}".format(menor)) 
    