# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# edad=int(input("Ingrese su edad : " ))

# if edad < 18:
#     print ("Es menor de edad")
# else:
#     print("Es mayor de edad")

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.    

# password=input("Ingrese su contraseña :" )  
# password=password.lower()
# passwordGuardada="pepito190"

# if password == passwordGuardada:
#     print("Es correcto")
# else:
#     print("Es incorrecto")

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# divisor=float(input("Ingrese un divisor  :" ))
# dividendo=float(input("ingrese un dividendo :" ))

# if divisor==0:
#     print("Error")
# else:
#     print(f"{divisor/dividendo}")

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# numero=int(input("Ingrese un numero :" ))
# if numero %2==0:
#     print("El numero es par")
# else:
#     print("Es impar")

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# edad=int(input("Ingrese su edad :" ))
# ingresos=float(input("ingrese sus ingresos mensuales :" ))

# if edad>16 and ingresos>=1000: 
#     print("Usted tiene que tributar")
# else:
#     print("Usted no tiene que tributar")    

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# nombre=input("Ingrese su nombre :" )
# sexo=input("Ingrese su sexo :" )

# letraDeNombre=nombre.lower()[0]
# grupoM=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
# grupoN=["n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# sexo=sexo.lower()

# if letraDeNombre in grupoM and sexo=="mujer"  :
#     print("Usted pertenece al grupo A.")
# elif letraDeNombre in grupoN and sexo=="hombre"or sexo=="varon"  :
#     print("Usted pertenece al grupo A.") 
# else:
#     print("Usted pertenece al grupo B.")     
   

# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	     5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€      	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# rentaAnual=float(input("Ingrese su renta anual : " ))

# if rentaAnual<10000:
#     print("Su tipo impositivo es de 5%.")
# elif rentaAnual>=10000 and rentaAnual<20000:
#     print("Su tipo impositivo es de 15%.") 
# elif rentaAnual>=20000 and rentaAnual<35000:
#     print("Su tipo impositivo es de 20%.")   
# elif rentaAnual>=35000 and rentaAnual<60000:
#     print("Su tipo impositivo es de 30%.") 
# else:
#     print("Su tipo impositivo es de 45%.")             


# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	    0.4
# Meritorio	    0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

# puntuacionUsuario=float(input("Ingrese la puntuacion del usuario : " ))

# if puntuacionUsuario==0.0:
#     print("El usuario tiene como rendimiento : inaceptable , le corresponde 0€ de beneficios.")
# elif puntuacionUsuario==0.4: 
#     print(f"El usuario tiene como rendimiento : aceptable , le corresponde {2400*puntuacionUsuario}€ de beneficios.")
# elif puntuacionUsuario>=0.6:
#     print(f"El usuario tiene como rendimiento : Meritorio , le corresponde {2400*puntuacionUsuario}€ de beneficios.")  


# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. 

# edad=int(input("Ingrese la edad del usuario : " ))

# if edad<4:
#     print("La entrada es gratis.")
# elif edad>=4 and edad<18:
#     print("La entrada cuesta 5€.")
# else:
#     print("La entrada cuesta 10€.")    


# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


# pizza=input("Ingrese si quiere pizza vegana o no : " )
# pizza=pizza.lower()
# if pizza=="si":
#     ingrediente=input("Ingrese 1 si desea Pimientos, o 2 si desea Tofu: " )
#     if ingrediente=="1":
#         print("Usted eligio pizza vegetariana con pimientos como ingrediente.")
#     else:
#         print("Usted eligio pizza vegetariana con Tofu comp ingrediente.")
# if pizza=="no":
#     ingredient=input("Ingrese 1 si desea Peperoni, 2 si desea jamon o 3 si desea Salmon : " )
#     if ingredient=="1":
#         print("Usted eligio pizza con Peperoni como ingrediente.")
#     elif ingredient=="2":
#         print("Usted eligio pizza con Jamon como ingrediente.")
#     else:
#         print("Usted eligio pizza con Salmon como ingrediente.")


    