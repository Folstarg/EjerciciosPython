# dar 2 palabras, calcular cual tiene mas vocales y mas consonantes.

nombre1=input("Ingrese el nombre 1 :")
nombre2=input("Ingrese el nombre 2 :")
nombre1vocales=0
nombre1consonantes=0
nombre2vocales=0
nombre2consonantes=0

for i in nombre1:
	i=i.lower()
	if i in "aeiou":
		nombre1vocales=nombre1vocales+1
	if i in "bcdfghjklmnñpqrstvwxyz":
		nombre1consonantes=nombre1consonantes+1	

for i in nombre2:
	i=i.lower()
	if i in "aeiou":
		nombre2vocales=nombre2vocales+1
	if i in "bcdfghjklmnñpqrstvwxyz":
		nombre2consonantes=nombre2consonantes+1	

if nombre1vocales>nombre2vocales:
	print(f"Tiene mas vocales : {nombre1}")
elif nombre1vocales<nombre2vocales:
	print(f"Tiene mas vocales : {nombre2}")	
else :
	print(f"Tienen las misma cantidad de vocales.")

if nombre1consonantes>nombre2consonantes:
	print(f"Tiene mas consonantes : {nombre1}")
elif nombre1consonantes<nombre2consonantes:
	print(f"Tiene mas consonantes : {nombre2}")	
else :
	print(f"Tienen las misma cantidad de consonantes.")	