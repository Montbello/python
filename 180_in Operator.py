
# in-Operator
# Gibt es "nur" in Python
# Membership operator
# Testet, ob ein Wert in einer Menge (Liste, String) ist
# Vergleichsoperator, der zu einem Boolean evaluiert (ausgewertet wird).

liste = [1, 4, 7, 9]
print(4 in liste)  # True

x = 7
if x in liste:
    print("Treffer")

print(3 in liste)  # False

# not in
print(3 not in liste)    # True (schönere Variante)
print(not (3 in liste))  # True

# Oft ein guter Ersatz für "or"
zahl = 11
print(zahl == 11 or zahl == 12 or zahl == 17)  # True
print(zahl in [11, 12, 17])                    # True

# in-Operator mit Strings
print("in-Operator mit Strings")
print("e" in "Hello")      # True
print("a" not in "Hello")  # True
print("Hell" in "Hello")   # True

