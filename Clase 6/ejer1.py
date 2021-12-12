# CLASE 6 - FUNCIONES
# Definir una funcion que me calcule cuanto voy a pagar una prenda
# que calcule el resultado y me lo retorne 

def calcular(p, d): # dos valores, precio y descuento
    print("Estoy en la funcion")
    descuento = (d / 100) * p  # d = descuento p= precio total descuento
    pagar = p - descuento 
    
    return pagar 


precio = int(input("Ingrese precio: "))
desc = int(input("Ingrese descuento (%): "))

resultado = calcular(precio, desc) #llamo a mi funcion calcular

print("a pagar: {}".format(resultado)) #imprimo el resultado por pantalla
