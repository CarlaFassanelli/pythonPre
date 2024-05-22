i = 0

while (i==0):
    frase = input ("Escriba una frase: ")
    cantidad = len (frase)
    if (cantidad > 15):
        print (frase)
    if (frase == "Aguante programaciòn"):
        print ("fin del programa")
        break