# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# palabra=input("Ingrese una palabra : " )

# for i in range(10):
#     print(palabra)


# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 

# edad=int(input("Ingrese la edad del usuario : " ) )

# for i in range(edad):
#     print(f"Cumple {i+1} años ")


# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# numero=int(input("Ingrese un numero entero positivo : " ))
# cadena=""

# for i in range(1,numero+1):
#     if i %2 != 0:
#         cadena=cadena+f"{i},"
# print(cadena)    
    
# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# numero=int(input("Ingrese un numero entero positivo : " ))
# cadenita=""
# for i in range(numero+1):
#     if i <=numero:
#         cadenita=cadenita+f"{numero-i},"
# print(cadenita)    


# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


# cantidadInvertida=float(input("Ingrese la cantidad invertida : " )) 
# InteresAnual=int(input("Ingrese el interes anual : " ))              
# cantidadAnios=int(input("Ingrese la cantidad de años : " ))          

# for i in range(cantidadAnios):
#     calculoInt=cantidadInvertida*InteresAnual/100
#     cantidadInvertida=cantidadInvertida+calculoInt
#     print(round(calculoInt,2))


# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

# numero=int(input("Ingrese un numero entero : " ))
# cadena=""
# for i in range(numero):
#     cadena=cadena+"*"
#     print(cadena)


# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# for i in range(1,11):
#     print(f"Esta es la tabla de {i}")
#     for j in range(1,11):
#         print(i*j)


# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# numero=int(input("Ingrese un numero entero : " ))
# cadena = ""


# for i in range(5):
#     cadena = f" {(numero)} " +cadena 
#     print( cadena )
#     numero=numero+2

# Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# contraseniaCorrecta="contraseña"
# contrasenia=""
# while contrasenia != contraseniaCorrecta:
#     contrasenia = input("Introduce la contraseña: ")
# print("Contraseña correcta")


# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# n = int(input("Introduce un número entero positivo mayor que 2: "))
# i = 2
# while n % i != 0:
#    i  += 1  #Esto es asi porque es igual que decir : i = i+1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")

# # Solucion 2.
    
# n = int(input("Introduce un número entero positivo mayor que 2: "))
# for i in range(2, n):
#     if n % i == 0:
#         break  #Esto se usa para romper el for y salir.
# if (i + 1)  == n:
#     print(str(n) + " es primo")
# else: 
#     print(str(n) + " no es primo")


# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# palabra=input("Ingrese una palabra : " )
# contador=0
# largoPalabra=len(palabra)-1
# for i in palabra:
#     palabra[0]
#     print(palabra[largoPalabra-contador])
#     contador+=1


# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.