# CLASE 10 - DICCIONARIOS
dic = {
       "nombre":"Agus",
       "apellido":"Perez",
       "edad": None,
       34.4: None
       }

# for a in dic:
#     print(a)
#     print(dic[a]) #iterar elementos de mi diccionario 

# for a in dic.values():
#     print(a)    # me itera solo los valores 

for a, b in dic.items(): # me retorna dos valores 
    print(a, b)