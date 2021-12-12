 # CLASE 6 - FUNCIONES


# Y = X2 + 4

def operacion(x):   # declarando la funcion y calculando el valor de x 
    print("Estoy en la funcion")
    # dentro de la funcion las variables
    # son accesibles solo dentro de la funcion 
    res = x * x + 4
    
    
    return res


x = int(input("Ingrese x: ")) #pedirle que me ingrese el valor de x 

resultado = operacion(x) #llamar la funcion 

print("El resultado es {}".format(resultado))


