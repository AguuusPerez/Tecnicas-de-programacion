# Clase 5 - Ejercitacion while 
# Leer un numero entero positivo desde teclado e imprimir 
# la suma de los digitos que lo componen


numero = int(input("Ingrese un numero positivo: "))
cantPares = 0 

while numero > 0:
    
    if numero%2 == 0:
        cantPares = cantPares + 1 
        
    suma = 0 
    while (numero != 0):
        digito = numero % 10
        suma = suma + digito        #Sumar todos los digitos que componen ese numero ingresado 
    
        numero =  numero // 10 
    
    print("Suma:" , suma) 
    
    numero = int(input("Ingrese un numero positivo: "))
  

print("Cantidad numeros pares: ", cantPares)   