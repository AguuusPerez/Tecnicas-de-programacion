# CLASE 5

# Leer un numero entero positivo desde teclado e 
# imprimir la suma de los digitos que lo componen
# determinar si es par o impar 
numero = int(input("Ingrese numero positivo: "))
cantidadPares = 0 

while numero > 0:
     
    if numero % 2 == 0:
        cantidadPares= cantidadPares + 1
        
    suma = 0
    while (numero != 0):
        digito = numero % 10
        suma = suma + digito
        
        numero = numero // 10
        
    print("Suma: {}".format(suma))
    
    numero = int(input("Ingrese numero positivo: "))

    

print("Cantidad numero pares: {}".format(cantidadPares))      