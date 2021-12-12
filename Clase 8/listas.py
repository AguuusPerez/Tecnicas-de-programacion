numeros = [1, 3, 5 , 7, 9]

mi_lista = ["a", "c", "f", True, 3.14, "h"]

print(numeros)

largo = len(numeros)
i = 0

while i < len(numeros):
    print(numeros[i])
    i = i + 1  # forma de imprimir elem de mi lista

print("imprimiendo con for()")
for item in numeros:
    print("una pasada")
    print(item)
    
    
# print(mi_lista)

# print(numeros[0])
# print(numeros[4])
# print(mi_lista[1]) #posicion 

# if "h" in mi_lista:
#     print("h esta en mi lista")
# else: 
#     print("no lo encontre")    

# largo = len(numeros)
# print(largo)

# print(len(mi_lista)) #longitud de mi lista

# mi_lista[2]="d" #cambiar 
# print(mi_lista) 

# mi_lista.append("e") #agregar al final
# print(mi_lista)   
# print(len(mi_lista))

# mi_lista.insert(2, "Hola") #insertar algo en un indice determinado
# print(mi_lista) 


# mi_lista.remove("Hola") #remover
# print(mi_lista)

# del mi_lista[0] #eliminar el primer elemento
# print(mi_lista)


# mi_lista.pop()
# print(mi_lista)

# mi_lista.reverse() #muestra en reversa mi lista
# print(mi_lista)
