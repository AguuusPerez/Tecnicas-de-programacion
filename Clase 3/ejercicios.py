import math # para que nos habilite todas las funciones posibles

# Calcular el primetro y area de un rectangulo ingresando su base y altura. 

base = int(input("Ingreso de la base: ")) # por defecto lo toma como un string, entonces le aclaramos que el num ingresado es un int
altura = int(input("Ingreso de la altura: "))

perimetro = base * 2 + altura * 2
area = base * altura 

print("El perimetro del rectangulo es {} y el area {} " .format(perimetro, area))




# Dado los catetos de un triangulo, calcular la hipotenusa. 

catetoa = int(input("Ingreso de cateto a: "))
catetob = int(input("Ingreso de cateto b: "))

hipotenusa = math.sqrt(catetoa ** 2 + catetob ** 2 ) 

print("La hipotenusa del triangulo ingresado es : {} ".format(hipotenusa))




"""  Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
 pregunte al usuario por la contrase;a e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
 que reside en la variable sin tener en cuenta la diferencia de mayusculas y minusculas """

password_valida = "12345"
 
password = input("Ingrese su contraseña: ")

if password == password_valida: 
    print("Password valida")
else: 
   print("Password erronea")    
 
 


"""En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículos y 5% si
compra hasta 20 artículos pero más de 10. Dado el precio unitario de un artículo y la
cantidad adquirida, muestre lo que debe pagar el cliente."""

precio_unitario = int(input("Ingrese precio unitario: "))
cantidad_producto = int(input("Ingrese cantidad de productos : ")) 

"""if cantidad_producto > 20 :
    descuento = 0.10
if cantidad_producto <= 20 and cantidad_producto >10 :
    descuento = 0.05
if cantidad_producto <= 10 :
    descuento = 0 """
    
if cantidad_producto > 20 :      #otra forma de resolverlo
     descuento = 0.10
else:
    if cantidad_producto > 10 :
        descuento = 0.05
    else: 
        descuento = 0
    
monto = precio_unitario*cantidad_producto*(1 - descuento) # restantole el descuento final

print("Monto a pagar {} con {}% de descuento".format(monto, descuento))
 