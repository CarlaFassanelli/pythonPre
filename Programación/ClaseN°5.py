con = True
while con == True:
    print("MENU:")
    print("1: Calcular aumento de sueldo")
    print("2: Ingreso a mi programa")
    print("3: Salir")
    valor= int(input("Ingrese una opcion: "))
    if valor == 1:
        sueldo = float(input("Sueldo: "))
        aumento = float(input( "Aumento: "))
        print("Nuevo sueldo: ", sueldo +(sueldo*aumento/100))
    elif valor == 2:
        empleado1 = input("ingrese un nombre: ")
        if empleado1 == "Carla":
            sueldo = 50000
            aumento = 25
            print("Nuevo sueldo: ", sueldo + (sueldo*aumento/100))
        elif empleado1 == "Pedro":
            sueldo = 150000
            aumento = 5
            print("Nuevo sueldo: ", sueldo + (sueldo*aumento/100))
    elif valor == 3:
        print("Gracias por usar el programa, vuelva pronto")
        break
    else:
        print("Error")
