# Examen pt2 - Tecnicas de programacion. 

dato = {                           # Diccionario con lo solicitado
        "nroParticipante":"",
        "nombre":"",
        "apellido":"",
        "edad":"",
        "sexo": "",
        "disparo nro": ""
        #"disparo nro 1": "",
        #"disparo nro 2": ""
        }

concurso = []                      # Lista para almacenar datos de los participantes
cantParticipantes = 0

while True:                         
    
    nroParticipante = int(input("Nro de participante: "))
    if nroParticipante == 999:      # Fin del ingreso en nroParticipante 999
        break                       
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (f/m): ")
    disparo = int(input("Disparo: "))
    #disparo1 = int(input("Disparo nro 1: "))
    #disparo2 = int(input("Disparo nro 2: "))
    
    cantParticipantes = cantParticipantes + 1   # Contador participantes 
    

    dato["nroParticipante"] = nroParticipante 
    dato["nombre"] = nombre
    dato["apellido"] = apellido
    dato["edad"] = edad
    dato["sexo"] = sexo
    dato["disparo nro"] = disparo
                            
    concurso.append(dato)

    dato = {                           
            "nroParticipante":"",
            "nombre":"",
            "apellido":"",
            "edad":"",
            "sexo": "",
            "disparo nro" : ""       
            }




print(concurso)  # PRINT DATO
print("Cantidad de partcipante: {}".format(cantParticipantes))   #PTO C