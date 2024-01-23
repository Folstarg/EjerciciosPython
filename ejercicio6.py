import math
try :
    continuar="1"
    while continuar=="1" or continuar=="2" or continuar=="3":
        if continuar=="1":
           numero1=float(input("Ingrese el numero 1:"))
        calcular=input("Ingresar 1 si queres sumar, 2 si queres restar, 3 multiplicar , 4 si queres dividir ,5 si queres elevar a la potencia o 6 si queres realizar la raiz cuadrada:")
        if calcular!="6" and continuar!="3":
            numero2=float(input("Ingrese el numero 2:"))
        if calcular=="1":
            resultado=numero1+numero2
            print(f"El resultado es {resultado}")
        elif calcular=="2":
            resultado=numero1-numero2
            print(f"El resultado es {resultado}")
        elif calcular=="3":
            resultado=numero1*numero2
            print(f"El resultado es {resultado}")   
        elif calcular=="4":
            if numero2==0:
                print("No se puede efectuar el calculo")
            else:
                resultado=numero1/numero2
                print(f"El resultado es {resultado}")
        elif calcular=="5":
            resultado=numero1**numero2
            print(f"El resultado es{resultado}")       
        elif calcular=="6":
            if numero1<0:
                print(f"No se puede efectuar el calculo")
            else:    
                resultado=math.sqrt(numero1)
                print(f"El resultado es {resultado}")    
        else:
            print(f"Valor incorrecto") 
        continuar=input("Si desea realizar otra operacion, ingrese 1, si quiere realizar otra operacion sobre el resultado, ingresa 2 ,Si desea realizar otra operacion con los numeros ya ingresados, ingrese 3 , sino , ingresar cualquier otro numero.")  
        if continuar=="2":
            numero1=resultado
except:
        print("Valor incorrecto")      
# Agregado1 : Hacer potencia.
# agregado2 : Hacer raiz cuadrada.
# agregado3 : Hacer que el programa no corte , preguntar al usuario si quiere realizar otra operacion.
# Agregado4 : Preguntarle al usuario si quiere realizar una operacion sobre el resultado.
# Agregado5 : Dar opcion al usuario de realizar otra operacion con los numeros ingresados.
        