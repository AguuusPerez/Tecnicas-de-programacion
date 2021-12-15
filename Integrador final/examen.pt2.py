#  Examen pt2 - Tecnicas de programacion

dato = {                           # Diccionario con lo solicitado
        "nroParticipante":"",
        "nombre":"",
        "apellido":"",
        "edad":"",
        "sexo": "",
        "disparo nro 1": "",
        "disparo nro 2": "",
        "mejorDisparo": ""
        }

concurso = []                      # Lista para almacenar datos de los participantes
cantParticipantes = 0
contFemenino = 0
acum = 0
acumDisparo = 0
acumMejorDisparo = 0

while True:                        # Carga de valores
    
    nroParticipante = int(input("Nro de participante: "))
    if nroParticipante == 999:      # Fin del ingreso en nroParticipante 999
        break                       
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (f/m): ")
    disparo1 = int(input("Disparo nro 1: "))
    disparo2 = int(input("Disparo nro 2: "))
    
    cantParticipantes = cantParticipantes + 1   # Contador participantes 
    
    if disparo1 < disparo2:      #Mejor disparo 
        mejorDisparo = disparo1
    if disparo2 < disparo1:
        mejorDisparo = disparo2
    
    dato = {                           
            "nroParticipante":"",
            "nombre":"",
            "apellido":"",
            "edad":"",
            "sexo": "",
            "disparo nro 1" : "",
            "disparo nro 2" : "",
            "mejorDisparo": ""
            }

    dato["nroParticipante"] = nroParticipante 
    dato["nombre"] = nombre
    dato["apellido"] = apellido
    dato["edad"] = edad
    dato["sexo"] = sexo
    dato["disparo nro 1"] = disparo1
    dato["disparo nro 2"] = disparo2
    dato["mejorDisparo"] = mejorDisparo
                            
    concurso.append(dato)
    
print(concurso) 

 # Mostrar el ganador 
ganador = 1000
ganadorID = ""
for item in concurso: 
    if item ["mejorDisparo"]  < ganador:
        ganador = item["mejorDisparo"]
        ganadorID= item["nroParticipante"]

for item in concurso:                           # PTO A 
    if item ["nroParticipante"] == ganadorID:
        print("El ganador es: ")
        print(item)   


# Mostrar el perdedor
perdedor = 0
perdedorID = ""
for item in concurso: 
    if item ["mejorDisparo"]  > perdedor:
        perdedor = item["mejorDisparo"]
        perdedorID= item["nroParticipante"]

for item in concurso:                           # PTO B 
    if item ["nroParticipante"] == perdedorID:
        print("El perdedor es: ")
        print(item)  

print("Cantidad de partcipantes que forman parte del concurso: {}".format(cantParticipantes))   # PTO C 

# Cantidad de mujeres que participan
for item in concurso:    
    if item ["sexo"] == "f":
        contFemenino = contFemenino + 1
        
print("Cantidad de mujeres que forman parte del concurso: {}".format(contFemenino)) # PTO D                


# Promedio edad de Hombres
cantMasculino =  cantParticipantes - contFemenino
for item in concurso: 
    if item ["sexo"] == "m":
        acum = acum + item["edad"]
        
print("Promedio de edad de Hombres: {}".format(acum/cantMasculino)) # PTO E

 
# Promedio de todos los disparos 
for item in concurso:
    acumDisparo = acumDisparo + item["disparo nro 1"] + item["disparo nro 2"]   

print("Promedio de todos los disparos: {}".format(acumDisparo/cantParticipantes))   # PTO F

# Promedio de los mejores disparos
for item in concurso: 
    acumMejorDisparo= acumMejorDisparo + item["mejorDisparo"]

print("Promedio de los mejores disparos: {}".format(acumMejorDisparo/cantParticipantes))    

