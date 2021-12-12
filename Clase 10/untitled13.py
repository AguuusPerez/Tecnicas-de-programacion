# CLASE 10 - DICCIONARIOS
dato = {
       "nombre":"",
       "apellido":"",
       "edad": None,
       }

nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

dato["nombre"] = nom
dato["apellido"] = ape
dato["edad"] = edad

for k,v in dato.items():
    print(v)
    