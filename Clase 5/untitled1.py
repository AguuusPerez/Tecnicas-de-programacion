#Se pide un programa que realice las siguientes acciones
#a) Pida el ingreso de 3 datos por teclado: el sueldo básico de cada empleado, la
#bonificación del mismo y si la misma está expresada en $ o en % (el fin de ingreso se
#indica con sueldo básico = 0) 
#b) Informe la cantidad de empleados
#c) Informe el sueldo básico promedio
#d) Informe el porcentaje de empleados que percibió alguna bonificación
#e) Informe el total pagado a los empleados (sueldo + bonif)



cant = 0
acum = 0 
cont = 0
acumSueldos = 0
basico = int(input("Ingrese el sueldo basico: "))

while basico != 0:
    
    bonif = int(input("Ingrese el sueldo bonificacion: "))
    tipo = (input("Ingrese el tipo de bonif ($ / %): "))
    
    cant = cant + 1 #pto B
       
    acum = acum + basico #pto C
    
    if bonif > 0:  #pto D #significa que el empleado recibio bonif
     cont = cont + 1
 
    #pto E
    if tipo =='$':
        bonifPesos = bonif 
    else: 
        bonifPesos = basico * bonif / 100  
        
    acumSueldos = acumSueldos + basico + bonifPesos                    
 
    
    basico = int(input("Ingrese el sueldo basico: "))
    
print("Cantidad de empleados: {}".format(cant))   
print("Promedio de basicos: {}".format(acum/cant)) # pto C - promedio
print("Porcentaje de empleados con bonif: {}%".format(cont/cant*100)) #pto D
print("Total pagado a los empleados: {}".format(acumSueldos))



