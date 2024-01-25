# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

saludo=input("¡Hola Mundo!")
print(saludo)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre=input("Cual es tu nombre?")
print(f"Hola,{nombre}")

# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((3+2)/(2*5))**2
 
print(f"El resultado es : {((3+2)/(2*5))**2}")

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas=int(input(" Cual es la cantidad de horas trabajadas? "))
costeHora=int(input(" Cual es el coste por hora? "))
print(f"La paga correspondiente es ${horasTrabajadas*costeHora}")

# Escribir un programa que lea un entero positivo,n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print(f"La suma de los primeros números enteros desde 1 hasta {n} es {suma}")

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso=input("Cuál es tu peso en kg?" )
estatura=input("Cuál es tu estatura en metros?" )
calculo=round(float(peso)/(float(estatura)**2))
print(f"El indice de masa corporal es de : {calculo}")

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n=int(input("Ingrese el numero dividendo :" ))
m=int(input("ingrese el numero divisor :" ))
print(f"{n}entre{m}da de cociente de : {n//m} y un resto de {n%m}")