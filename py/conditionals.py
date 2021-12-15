# x = 30

# if x < 20:
#     print("x es menor que 20")
# else:
#     print("x es mayor que 20")

# color = "asd"

# if color == "red":
#     print("El color es rojo!")
# elif color == "blue":
#     print("El color es azul")
# else: 
#     print("Cualquier color!")

name = "J"
lastname = "Carte"

if name == "John":
    if lastname == "Carter":
        print("Tu eres John Carter")
    else: print("Tu no eres John Carter")
else: 
    print("Tu no eres John")       







def bonificacion(sbasico, bonif, tipo):
    
    if tipo == "$": 
         bonifPesos= bonif   #basico + bonificacion
    else: 
         bonifPesos = sbasico * bonif / 100
         
    total = sbasico + bonifPesos   
    
    return  total   

cant = 0
acum = 0
cont = 0
acumSueldos = 0
basico = int(input("Ingrese el sueldo basico: "))

while basico != 0:
    
    bonif = int(input("Ingrese la bonificacion: ")) 
    tipo = input("Ingrese el tipo de bonif ($ / %): ")
    
    cant = cant + 1 #pto b cantidad de empleados
    
    
    acum = acum + basico #pto c promedio
    
    #punto d
    if bonif > 0: #significa que el empleado recibio bonif
        cont = cont + 1
        
    #punto e 
    resultado = bonificacion(basico, bonif, tipo) 
    acumSueldos = acumSueldos + resultado  #suma el sueldo basico mas bonificacion 
    
    basico = int(input("Ingrese el sueldo basico: "))

print("Cantidad de empleados: {}".format(cant))    #pto b cantidad de empleados
print("Promedio de basicos: {}".format(acum/cant)) #pto c sueldo promedio
print("Porcentaje de empleados con bonificacion: {}%".format(cont/cant*100)) #pto d porcentaje
print("Total pagado a los empleados: {}".format(acumSueldos))