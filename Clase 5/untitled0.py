# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:21:52 2021

@author: Agus
"""


dato = {"nroPart": '',
        "nombre": '',
        "apellido": '',
        "edad": '',
        "sexo":'',
        "disparo":''
        }

concurso = [] # Lista vacia para almacenar los participantes 
cantPart = 0

while True:
    
    nroPart = int(input('Nro de participante: '))
    if nroPart == 999:
        break
    
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    edad = int(input('Edad: '))
    sexo = input('Sexo (f/m): ')
    disparo = int(input('Disparo: '))
    
    
    cantPart = cantPart + 1
    
    dato['nroPart']= nroPart
    dato['nombre']= nombre
    dato['apellido']= apellido
    dato['edad']= edad
    dato['sexo']= sexo
    dato['disparo']= disparo
    concurso.append(dato)
    
 #Procesamiento de informacion    
    
print(concurso)   
#punto C
print('Cantidad de participantes: {}'.format(cantPart))  

#punto D
for item in concurso:
    print(item)
    if item['sexo'] == 'm':
        contMasc = contMasc + 1

print('Cantidad de masculinos: {}' .format(contMasc))        
    
    