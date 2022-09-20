
# Funktionen
# Schlüsselwort zum Erzeugen einer Funktion: def
# Vorteil: Kann mehrmals ausgeführt werden

# Funktionsdefinition
def meine_erste_funktion():
    print("Hallo, ich bin eine Funktion!")

# Funktionsaufruf
meine_erste_funktion()  # Hallo, ich bin eine Funktion!
meine_erste_funktion()  # Hallo, ich bin eine Funktion!
meine_erste_funktion()  # Hallo, ich bin eine Funktion!

# Parameter und Argumente
# Parameter stehen in der Funktionsdefinition
def f(para):
    print("Hello", para)

# Argumente sind die Werte, die einer Funktion übergeben werden
f("Peter")  # Hello Peter
f("Paul")   # Hello Paul
f("Mary")   # Hello Mary
# f(input("Bitte etwas eingeben!"))
f(42)       # Hello 42

# Rückgabe durch return
# Eine Funktion, die zwei Argumente erwartet und einen Wert zurück gibt:
def addiere(x, y):
    ergebnis = x + y
    return ergebnis

print(addiere(3, 4))  # 7

addiere(7, 9)  # Dieser Wert verfällt

res = 9
res = res + addiere(7, 9)
print(res)  # 25

wert = addiere(17, 19)
print(wert)  # 36

# Standard-Parameter (Standard-Wert für Parameter)
# Allen Parametern, die keinen Standard-Wert haben, muss ein Argument übergeben werden.
# Die Parameter mit Default-Werten müssen am Ende stehen
def addiere(x, y=1):
    return x + y

print(addiere(7))     # 8
print(addiere(2, 6))  # 8
# print(addiere())  # TypeError: addiere() missing 1 required positional argument: 'x'





