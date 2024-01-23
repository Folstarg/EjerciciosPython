heroe=input("Ingrese el nombre de su heroe :")
villano=input("Ingrese el nombre de su villano :")
if len(heroe)>len(villano):
    print("El nombre mas largo es el de : Heroe")
elif len(heroe)<len(villano):
    print("El nombre mas largo es el de : Villano")
else :print("Ambos nombres tienen la misma canidad de letras")
