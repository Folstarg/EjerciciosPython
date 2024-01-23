heroe=input("Ingrese el nombre de su heroe:")
heroeAP=int(input("Ingrese el Poder de ataque de su heroe:"))
villano=input("Ingrese el nombre de su villano:")
villanoAP=int(input("Ingrese el Poder de ataque de su villano:"))
if heroeAP>villanoAP:
    print("El heroe gana")
elif heroeAP<villanoAP:
    print ("El villano gana")
else:print("Seria un empate")


