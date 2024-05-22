variable1 = "hola"

número = 5

flotante = 1.2

negativo = -5 

bbooleano = True 

# operadores aritméticos

a = 5
b = 4

# suma 

resultado = a + b 
print (resultado) 


# resta 

resultado = a - b
print (resultado)


# multiplicación

resultado = a * b
print (resultado)

# división

resultado = a / b
print (resultado)


# potenciación

resultado = a ** b
print (resultado)

# menor que 
resultado = a <= b

# mayor que 
resultado = a >= b

# condicionales

# if # sirve para comparar #si 

Carla = 5.000
Franco = 4.000
if Carla >= Franco: 
    print("Carla ganá más")

# elif # sirve para caso contrario #si no
elif Franco >= Carla:
    print("Franco ganá más")

# else # el resto
else:
    print("error")



#entrada de usuario
# entrada básica
entrada = input ("ingresar nombre: ")
print (entrada)

# entrada cadena de texto 
entrada = str (input ("ingresar nombre: "))
print (entrada)

#número entero 
entrada = int (input ("ingresar nombre: "))
print (entrada)

# número flotante
entrada = float (input ("ingresar nombre: "))
print (entrada)


# bucles

# dos tipos de bucles

# while # mientras sea verdad el código se va a ejecutar

# for # se ejecuta una cierta cantidad de veces especificada

# ejemplos

test1 = 5
print (test1)
while True:
    if test1 >= 0:
        test1 -=1
        print (test1)

for i in range (5):
    i +=1
    print (i)

#fstring se usa para texto personalizado
nombre = input ("ingresar nombre: ")
print (f"hola {nombre}")





