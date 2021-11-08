# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:44:41 2021

@author: Agus
"""

# Este es un programa simple 
""" print("Bienvenido") # "" o '' es un string o cadena de caracteres 

mi_passw = '12345'

passw = input("Ingrese password: ")


if passw == mi_passw:
    print("Password correcta")
    print("Estoy adentro del if TRUE")
else:
    print("Password incorrecta")
    print("Estoy adentro del ELSE")

print('Saliendo del programa')    """


# contrasena erronea, y que te vuelva a preg 
print("Bienvenido") 

mi_passw = '12345'
cont = 0

passw = input("Ingrese password: ")

while mi_passw != passw :            #me repite el bucle hasta poner la password correcta
    cont = cont + 1      # cantidad de veces que intente ingresar la contrasena
    if cont == 3 :
        break            #break me saca del primer bucle 
        
    print("Password incorrecta")
    print("Le queda {} intentos" .format(3-cont))
    passw = input("Ingrese password: ")

if  cont == 3: 
    print('Tarjeta bloqueada')
else:
    print ('Password correcta')
    
print("Numero de intentos: {}" .format(cont))
print('Saliendo del programa') 
 

























