#  Examen pt1 - Tecnicas de programacion

def sueldoBono(basico, antiguedad):
    
    if  antiguedad >= 1 and antiguedad <= 5:
        bonifBono = basico * 10 / 100 
        
    elif antiguedad >= 5 and antiguedad <=10:
         bonifBono = basico * 20 / 100
        
    elif antiguedad > 10:
         bonifBono = basico * 30 / 100
    else: 
        bonifBono = 0
        
    total = basico + bonifBono 
         
    return total

cant = 0
acum = 0
acumAntiguedad = 0
contFem = 0 
acumSueldosAntiguedad = 0 
sueldoAlto = 0
mayorEdad = 0
menorEdad = 999
basico = int(input("Ingrese el sueldo basico: "))

while basico != 0:
        
    cant = cant + 1 #cantidad empleados
      
    edad = int(input("Ingrese su edad: "))

    if edad > mayorEdad:
         mayorEdad = edad 
    if edad < menorEdad:
        menorEdad = edad
 
     
    sexo = input("Ingrese si es femenino o masculino: ")
    
    if sexo == "femenino": #porcentaje de mujeres trabajando
        contFem = contFem + 1
    
    antiguedad = int(input("Ingrese su antiguedad: "))
    
    resultado = sueldoBono(basico, antiguedad)
    acumSueldosAntiguedad = acumSueldosAntiguedad + resultado
    
   # Informar el sueldo total más alto (básico + bono) 
    if resultado > sueldoAlto:
        sueldoAlto = resultado 
        

    acum = acum + basico #promedio
    
    basico = int(input("Ingrese el sueldo basico: ")) 

    acumAntiguedad = acumAntiguedad + antiguedad
        
    
         
print("Cantidad de empleados: {}".format(cant))
print("Promedio de sueldos basicos: {}".format(acum/cant))
print("Promedio de antiguedad de todos los empleados es: {}".format(acumAntiguedad/cant))
print("Porcentaje de mujeres trabajando es: {}%".format(contFem/cant*100)) 
print("El sueldo total promedio es: {}".format(acumSueldosAntiguedad/cant))
print("El sueldo total mas alto es: {}".format(sueldoAlto))
print("El empleado mas joven es {}" .format(menorEdad))
print("El empleado mas mayor es {}" .format(mayorEdad))
