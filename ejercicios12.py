# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

def tabla(numero):
    tablaDeMultiplicar=open(f"tabla {numero}.txt","w")
    for i in range(1,11):
        tablaDeMultiplicar.write(f"{numero} X {i} = {numero*i}\n")
    tablaDeMultiplicar.close()

tabla(2)  


# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


def buscadorTabla(numero):
    try:
        tablaMultiplicar=open(f"tabla {numero}.txt")
        print(tablaMultiplicar.read()) 
        tablaMultiplicar.close()  
    except:
        print(f"El fichero tabla {numero}.txt no existe.")

# buscadorTabla(8)


# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello .


def lectoraDeTablas(n,m):
    try:
        tablaMultiplicar=open(f"tabla {n}.txt")
        palabra=tablaMultiplicar.readlines()
        print(palabra[m-1])
        tablaMultiplicar.close()  
    except:
        print(f"El fichero tabla {n,m}.txt no existe.")


# lectoraDeTablas(3,5)


# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

url=input("Ingrese el url : " )
simbolos = ['¿','?','.','.',';',':','¡','!']
numpalabras = 0
with open(f"{url}", 'r') as fichero:
    for linea in fichero:
        for simbolo in simbolos:
            linea = linea.replace(simbolo,' ')
        palabras = linea.split()
        for palabra in palabras:
            numpalabras += 1
print(f'El texto contiene {numpalabras} palabras' )

# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.