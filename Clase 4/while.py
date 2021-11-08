


i = 0

while i < 5:    #mientras
     print("Hola mundo desde Python")
     i = i + 1   #contador o incrementador de a 1
     




# calcular promedio de 5 notas de un alumno
'''i = 0
acum = 0


while i < 5:    #mientras
     nota = int(input("Nota: "))
     
     acum = acum + nota  #incrementador de nota
     i = i + 1   #contador o incrementador de a 1
     
promedio = acum / 5 
     
print("El promedio de notas es: {}" .format(promedio))          
print('Fin del programa')     '''


#Sacar promedio de notas y calcule el prom de esas notas (NO TIENE condicion de fin ) 

i = 0 
acum = 0
contProm = 0
contDesap = 0

nota = int(input("Ingrese nota: "))

while (nota <=0 or nota > 10) and nota !=99:
    print("Ingresaste una nota no valida")
    nota = int(input("Ingrese nota nuevamente: "))
    
while nota != 99 : #(fin que impuse yo) 
      acum = acum + nota  #acumulador de nota 
      i = i + 1           #contador o incrementador de a 1 
      
      if nota >= 7 :      # contar los que promocionan 
          contProm = contProm + 1  
      if nota <4 :
          contDesap = contDesap + 1 # contar los que desaprueban
                 
      nota = int(input("Ingrese nota: "))
      while (nota <=0 or nota > 10) and nota !=99:
          print("Ingresaste una nota no valida")
          nota = int(input("Ingrese nota nuevamente: b"))
      
      
      
           
promedio = acum / i          #promedio de notas totales

print("La cantidad de notas ingresadas es: {}".format(i))
print("La cantidad de personas que promocionan es: {}".format(contProm))
print("La cantidad de personas que desaprobaron es: {}" .format(contDesap))
print("El promedio de notas es: {}" .format(promedio))          
print('Fin del programa') 







      