# Un progama que pida los animes que se guardan, se cargara los que esten.

cantidadAnimes=int(input("Ingrese la cantidad de animes que quiera ingresar :"))
contador=0
lista=[]
while contador<cantidadAnimes:
    contador=contador+1
    nombreAnime=input("Ingrese el nombre del anime :")
    lista.append(nombreAnime)
print(lista)    