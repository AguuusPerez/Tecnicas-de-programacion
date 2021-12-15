demo_list = [1, "hello", 1.34, True, [1 ,2 ,3]]
colors = ["red", "green", "blue", "red"]

number_list = list((1 ,2 ,3 ,4))
# print(type(number_list))

# r = list(range(1, 11)) #rango, quiero crear una lista que vaya del 1 al 10, la guardamos en una variable 
# print(r) 

# print(dir(colors)) # dir, muestra todas las fnciones que puedp hacer con esta lista
# print(len(colors)) # longitud de esta lista 
# print(colors[1]) # me muestra el dato posicionado en 1
# print(colors[-1]) #me muestra el indice inverso
# print("green" in colors) # green esta en colors? devuelve un boolean

# print(colors)
# colors[1] = "yellow" #cambiar de colors en la posicion 1, por yellow
# print(dir(colors)) #imprime metodos de lo que pidamos 

# colors.append("violeta") #agregar un nuevo elemento 
# colors.extend(["violeta", "yellow"]) #agregar dos elementospor separado pero adentro de una tupla o lista

# colors.insert(1, "violet") #insertar en tal posicion tal valor
# colors.insert(len(colors), "violet") #insertar justo al final de mi lista el valor violet
# print(colors)

# colors.pop() #quitar el ultimo valor agregado
# colors.remove("green") #quitar un valor en especifico 
# colors.clear #limpia por completo mi lista

# colors.sort() #ordena mi lista alfabeticamente
# colors.sort(reverse=True) #ordena mi lista de forma inversa
print(colors.index("red")) #muestra posicion
print(colors.count("red")) #contar cuantas veces esta el valor red

