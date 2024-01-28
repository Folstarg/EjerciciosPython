# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


nombre=input("Cual es tu nombre ?" )
numero=int(input("Ingrese un numero :" ))

for i in range(numero):
    print(f"{nombre}")