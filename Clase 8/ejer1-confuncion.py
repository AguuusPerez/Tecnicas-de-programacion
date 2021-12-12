#Se pide un programa que realice las siguientes acciones
#a) Pida el ingreso de 3 datos por teclado: el sueldo bÃ¡sico de cada empleado, la
#bonificaciÃ³n del mismo y si la misma estÃ¡ expresada en $ o en % (el fin de ingreso se
#indica con sueldo bÃ¡sico = 0) 
#b) Informe la cantidad de empleados
#c) Informe el sueldo bÃ¡sico promedio
#d) Informe el porcentaje de empleados que percibiÃ³ alguna bonificaciÃ³n
#e) Informe el total pagado a los empleados (sueldo + bonif)

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