# CLASE 10 - DICCIONARIOS
dic = {
       "nombre":"Agus",
       "apellido":"Perez",
       "edad": None,
       34.4: None
       }

print(dic)
print(type(dic))
print(len(dic))

print(dic["apellido"])
# si no lo encuentra, retorna Error

print(dic.get("edad"))
# Si no lo encuentra, retorna None


dic["edad"] = 25
print(dic)

dic["dni"] = 39642213
print(dic)

dic["profesion"]= "Ingeniera"
print(dic)

dic.pop(34.4)
print(dic)  #eliminar una key

del dic["edad"]
print(dic) #eliminar edad

dic.clear()
print(dic)



