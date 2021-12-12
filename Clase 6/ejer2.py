 # CLASE 6 - FUNCIONES

def menu():
    print("Bienvenido!!")
    print("Ingrese 1 para ver su saldo")
    print("Ingrese 2 para transferir")
    print("Ingrese 3 para salir")
    
    opcion = int(input("opcion: "))
    
    return opcion  


while True:
    opcion = menu ()

    if opcion == 1:
        print("Su saldo es $0")
    
    elif opcion == 2:
        print("Usted esta transfiriendo") 
    
    elif opcion == 3:
        print("Chau!")
        break             #saliendo
    else:
        print("Usted ingreso cualquier cosa")
        break             # si aprestaste cualquier numero que no este, salir
    
print("Saliendo")    









