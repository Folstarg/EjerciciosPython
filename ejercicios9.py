# # Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


# nombre=input("Cual es tu nombre ?" )
# numero=int(input("Ingrese un numero :" ))

# for i in range(numero):
#     print(f"{nombre}")


# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
    
# nombreCompleto=input("Ingrese nombre completo :" ) 
# print(nombreCompleto.lower())
# print(nombreCompleto.upper())
# print(nombreCompleto.title())    

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


# nombre=input("Cual es tu nombre?")
# print(nombre.upper())
# print(f"Cantidad de letras es :{len(nombre)}")

# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

# numeroCompuesto=input("Ingrese el numero entero : " )
# numerocompu=numeroCompuesto.split("-")
# print(numerocompu[1])

# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

# frase=input("Ingrese una frase :" )
# fraseGay=frase[::-1]
# print (f"{fraseGay}")

# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# frase=input("Ingrese una frase :" )
# vocal=input("Ingrese una vocal :" )
# fraseConVocal=frase.replace(vocal, vocal.upper())
# print(fraseConVocal)