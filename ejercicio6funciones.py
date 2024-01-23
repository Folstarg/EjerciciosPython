
import math

def respuesta(valor):
    print(f"El resultado es {valor}")

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        print("No se puede efectuar el calculo")
    else:
        return a/b
    
def potencia(a,b) :
     return a**b  

def raizcuadrada(a):
    if a<0:
        print("No se puede efectuar el calculo")
    else:    
      return math.sqrt(a)
                
try :
    continuar="1"
    while continuar=="1" or continuar=="2" or continuar=="3":
        if continuar=="1":
           numero1=float(input("Ingrese el numero 1:"))
        calcular=input("Ingresar 1 si queres sumar, 2 si queres restar, 3 multiplicar , 4 si queres dividir ,5 si queres elevar a la potencia o 6 si queres realizar la raiz cuadrada:")
        if calcular!="6" and continuar!="3":
            numero2=float(input("Ingrese el numero 2:"))
        if calcular=="1":
            resultado=sumar(numero1,numero2)
            respuesta(resultado)
        elif calcular=="2":
            resultado=restar(numero1,numero2)
            respuesta(resultado)
        elif calcular=="3":
            resultado=multiplicar(numero1,numero2)
            respuesta(resultado)  
        elif calcular=="4":
            resultado=dividir(numero1,numero2)
            respuesta(resultado)
        elif calcular=="5":
            resultado=potencia(numero1,numero2)
            respuesta(resultado)       
        elif calcular=="6":
            resultado=raizcuadrada(numero1)
            respuesta(resultado)    
        else:
            print("Valor incorrecto") 
        continuar=input("Si desea realizar otra operacion, ingrese 1, si quiere realizar otra operacion sobre el resultado, ingresa 2 ,Si desea realizar otra operacion con los numeros ya ingresados, ingrese 3 , sino , ingresar cualquier otro numero.")  
        if continuar=="2":
            numero1=resultado
except:
        print("Valor incorrecto")      

        