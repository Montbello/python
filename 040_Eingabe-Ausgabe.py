
# Eingabe & Ausgabe

vorname = "Cord"
nachname = "Mählmann"
# Kommaseparierte Liste
print(vorname, nachname)  # Cord Mählmann

# Separator (Standard ist das Leerzeichen)
print(1, 2, 3)  # 1 2 3
# Die benannten Argumente/Parameter müssen am Ende stehen
print(1, 2, 3, sep="-")  # 1-2-3
print(1, 2, 3, sep="")   # 123

# Ende (Standard ist der Zeilenumbruch: \n)
print("Hello", end=" ")
print("brave", end=" ")
print("new", end=" ")
print("World")  # Hello brave new World

print("Guten\nTag")
# Guten
# Tag

# Eingabe
# input()
name = input("Bitte Namen eingeben!\n")
print("Hallo", name)  # Hallo Cord

# alter = int(alter)













