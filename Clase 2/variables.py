print("Hola mundo")
print("Bienvenido")
print('texto con comillas simples')  # imprimir una frase / palabra 

resultado = input("Ingrese su contraseña")
print('Saliendo del programa')

mi_variable = 5

pepito =  30
pepita = " 30"
dato = 56.6

frase = "esta es una frase"

print(pepito)  # imprimir el contenido de una variable
print(frase) 
print("frase") # imprimo algo en pantalla entre comillas

resultado1 = pepito + dato + 1000   # sumar variables
print(resultado)

resultado2 = pepito - mi_variable  # restar variables
print(resultado2) 


resultado3 = frase + "_Holaa_" + pepita  # concatenacion (solo con string)
print(resultado3) 

resultado4 = pepito + int(pepita) # casteo pepita string en numero
print(resultado4)

resultado5 =  str(pepito) + pepita  #  casteo pepito un entero en string
print(resultado5)


print("El resultado es: {} - {}" .format(resultado5, resultado4))  # muestra el resultado dentro de los {}

# casteo
# str -> casteo un entero en string 
# int o float -> casteo un string en un numero

