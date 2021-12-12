# CLASE 12 - TIPO PARCIAL

dato = {                           # Diccionario con lo solicitado
        "nroParticipante":"",
        "nombre":"",
        "apellido":"",
        "edad":"",
        "sexo": "",
        "disparo nro" : ""       
        }

concurso = []                       # Lista para almacenar datos de los participantes
cantParticipantes = 0
contMasculino = 0
acum = 0
acumDisparo = 0

while True:                         # Carga de valores   
    
    nroParticipante = int(input("Nro de participante: "))
    if nroParticipante == 999:      # Fin del ingreso en nroParticipante 999
        break                       
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (f/m): ")
    disparo = int(input("Disparo nro: "))
    #disparo1 = int(input("Disparo nro 1: "))
    #disparo2 = int(input("Disparo nro 2: "))
    
    cantParticipantes = cantParticipantes + 1   # Contador participantes 
    
    dato = {                           
            "nroParticipante":"",
            "nombre":"",
            "apellido":"",
            "edad":"",
            "sexo": "",
            "disparo nro" : ""       
            }
    
    dato["nroParticipante"] = nroParticipante 
    dato["nombre"] = nombre
    dato["apellido"] = apellido
    dato["edad"] = edad
    dato["sexo"] = sexo
    dato["disparo nro"] = disparo
                            
    concurso.append(dato)

 # Mostrar el ganador 
ganador = 1000
ganadorID = ""
for item in concurso: 
    if item ["disparo nro"]  < ganador:
        ganador = item["disparo nro"]
        ganadorID= item["nroParticipante"]

for item in concurso:                           # PTO A 
    if item ["nroParticipante"] == ganadorID:
        print("El ganador: ")
        print(item)

 








print(concurso)           # print dato
print("Cantidad de partcipantes que forman parte del concurso: {}".format(cantParticipantes))  #PTO C

# Cantidad de Masculinos que participan
for item in concurso:     
    if item ["sexo"] == "m":
        contMasculino = contMasculino + 1        
        
print("Cantidad de masculinos que forman parte del concurso: {}".format(contMasculino))  # PTO D

# Promedio de edad de Mujeres
cantFemenino =  cantParticipantes - contMasculino 
for item in concurso: 
    if item ["sexo"] == "f":
        acum = acum + item["edad"]
        
print("Promedio de edad de Mujeres es: {}".format(acum/cantFemenino)) # PTO E     
 
# Promedio de todos los disparos
for item in concurso:
    acumDisparo = acumDisparo + item["disparo nro"]       

print("Promedio de disparos: {}".format(acumDisparo/cantParticipantes))   # PTO F
        
        