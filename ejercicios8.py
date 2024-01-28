# # Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

# print("¡Hola Mundo!")

# # Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

# saludo=input("¡Hola Mundo!")
# print(saludo)

# # Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

# nombre=input("Cual es tu nombre?")
# print(f"Hola,{nombre}")

# # Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((3+2)/(2*5))**2
 
# print(f"El resultado es : {((3+2)/(2*5))**2}.")

# # Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

# horasTrabajadas=int(input(" Cual es la cantidad de horas trabajadas?" ))
# costeHora=int(input(" Cual es el coste por hora? "))
# print(f"La paga correspondiente es ${horasTrabajadas*costeHora}." )

# # Escribir un programa que lea un entero positivo,n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

# n = int(input("Introduce un número entero:" ))
# suma = n * (n + 1) / 2
# print(f"La suma de los primeros números enteros desde 1 hasta {n} es {suma}.")

# # Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# peso=input("Cuál es tu peso en kg?" )
# estatura=input("Cuál es tu estatura en metros?" )
# calculo=round(float(peso)/(float(estatura)**2))
# print(f"El indice de masa corporal es de : {calculo}.")

# # Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
# n=int(input("Ingrese el numero dividendo :" ))
# m=int(input("ingrese el numero divisor :" ))
# print(f"{n} entre {m} da de cociente de {n//m} y un resto de {n%m}.")

# # # Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# plata=int(input("Ingrese la cantidad que desea invertir :" ))
# interesAnual=int(input("Ingrese la cantidad del interes anual :" ))
# cantidadAños=int(input("Ingresa la cantidad de años :" ))

# for i in range(cantidadAños):
#     interes=plata*interesAnual/100
#     plata=plata+interes

# print(f"El capital obtenido en la inversión es {plata}")   
    

# # # Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


# cantidadPayasos=(int(input("Ingrese la cantidad de payasos en su envio :" )))
# cantidadMunecas=(int(input("Ingrese la cantidad de muñecas en su envio :" )))
# pesoPayaso=112
# pesoMuneca=75
# paquete=cantidadPayasos*pesoPayaso+cantidadMunecas*pesoMuneca
# print(f"El paquete pesa {paquete} g")

# # Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# ahorros=int(input("Ingrese la cantidad ahorrada :" ))
# interesAnual=4
# cantidadAños=3

# for i in range(cantidadAños):
#     interes=ahorros*interesAnual/100
#     ahorros=ahorros+interes
#     print(f"El capital obtenido en la inversión es {round(ahorros,2)}")

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

cantidadpanNoHoy=int(input("Ingrese la cantidad de pan que no es del dia :" ))
print("PrecioPan=3.49€")
print("El descuento por no ser fresco es de 60%")

precioPan=3.49
panNoHoy=precioPan-precioPan*60/100
costeFinal=cantidadpanNoHoy*panNoHoy
print(f"El coste final es {round(costeFinal,2)}€")