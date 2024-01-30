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

# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

# mail=input("Ingrese el email :" )
# mailPiola=mail.split("@")
# mailPiola=mailPiola[0]+"@ceu.es"
# print(mailPiola)

# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

# precio=input("Ingrese el precio del producto en euros :" )
# precioEu=precio.split(".")
# precioEuEntero=precioEu[0]
# precioEuDecimales=precioEu[1]
# print(f"El numero entero es : {precioEuEntero} y el numero de céntimos es {precioEuDecimales}" )

# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

# fecha=input("Ingrese la fecha de su nacimiento en formato dd/mm/aaaa :" )
# fechaNacimiento=fecha.split("/")
# fechaDia=fechaNacimiento[0]
# fechaMes=fechaNacimiento[1]
# fechaAnio=fechaNacimiento[2]
# print(f"dia {fechaDia}, mes {fechaMes} y año {fechaAnio}") 

# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas
# , y muestre por pantalla cada uno de los productos en una línea distinta.

# productos=input("Ingrese los productos de la cesta de compra separados por comas :" ) #arroz,queso,
# prodcutosEnCesta=productos.split(",")
# for i in prodcutosEnCesta:
#     print(i)

# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
#  y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre=input("Ingrese el nombre del producto :" )
precio=input("Ingrese el precio del producto :" )
unidades=input("ingrese la cantidad de unidades del producto :" )
cantidadDeCerosASumar="" 
precioEntero=precio.split(".")
cerosFaltantes=6-len(precioEntero[0])

for i in range(cerosFaltantes):
   cantidadDeCerosASumar=cantidadDeCerosASumar+"0"

preciounitario=cantidadDeCerosASumar+precio #22
print(preciounitario)

unidadesDeCerosASumar=""
unidades3Digitos=3-len(unidades)
for i in range(unidades3Digitos):
   unidadesDeCerosASumar=unidadesDeCerosASumar+"0"

unidades3Digitos=unidadesDeCerosASumar+unidades   
print(unidades3Digitos)

precioEnNumero=float(precio)
unidadesEnNumero=int(unidades)
costeTotal=precioEnNumero*unidadesEnNumero
costeTotal=str(costeTotal)

costeTotalCeros=""
costeTotalConEnteros=costeTotal.split(".")
cerosFaltantesEnCosteTotal=8-len(costeTotalConEnteros[0])
for i in range(cerosFaltantesEnCosteTotal):
    costeTotalCeros=costeTotalCeros+"0"
costeTotal=costeTotalCeros+costeTotal
print(costeTotal)


   
