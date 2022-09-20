
# Listen-Methoden
# Eine Methoden gehört zu einem Objekt
# und werden mit einem Punkt hinter das Objekt geschrieben.
# Eine Funktion kann ganz alleine stehen, so wie z.B. print()

# append() zum Anhängen eines neuen Elements
liste1 = [3, 7, 23, 42]
print(liste1)            # [3, 7, 23, 42]
liste1.append(77)
print(liste1)            # [3, 7, 23, 42, 77]
print(type(liste1))      # <class 'list'>

"""
Fiktive Sprache:
append(liste1, 77)
"""

# insert(pos, wert)
# Fügt wert an der Position pos ein.
# Die Liste wird neu indiziert.
liste1.insert(0, 13)  # [13, 3, 7, 23, 42, 77]
print(liste1)
liste1.insert(3, 37)  # [13, 3, 7, 37, 23, 42, 77]
print(liste1)

# count(element)
# Gibt zurück, wie oft das Element vorkommt
liste2 = [7, 5, 3, 7, 9, 2, 7]
print(liste2.count(7))  # 3

# reverse()
# Dreht die Liste um
liste3 = [1, 2, 3, 4, 5]
liste3.reverse()
print(liste3)  # [5, 4, 3, 2, 1]

# index(element)
# Gibt den ERSTEN Index von element zurück
liste4 = [0, 1, 2, 3, 4, 5, 6, 7, 4]
print(liste4.index(4))  # 4
liste5 = [3, 7, 23, 42, 77]
print(liste5.index(3))  # 0
print(liste5[0])        # 3
liste5[0] = 99
print(liste5)  # [99, 7, 23, 42, 77]

liste6 = ["Hund", "Katze", "Maus", "Schaf", "Tralala"]
print(liste6.index("Maus"))  # 2
# Wenn es das Element nicht gibt
# print(liste6.index("Bär"))  # ValueError: 'Bär' is not in list

# pop([index]) - Die eckigen Klammern bedeuten optional
# Gibt das Element an index zurück UND entfernt es aus der Liste.
# Der Standard ist das letzte Element.
liste7 = [0, 1, 2, 3, 4, 5]
print(liste7.pop())   # 5
print(liste7)         # [0, 1, 2, 3, 4]
print(liste7.pop(2))  # 2
print(liste7)         # [0, 1, 3, 4]
liste7.pop()
liste7.pop()
print(liste7)  # [0, 1]
zahl = liste7.pop()
print(zahl)    # 1
print(liste7)  # [0]
liste7.pop()
print(liste7)  # []
# liste7.pop()   # IndexError: pop from empty list

# remove(element)
# Entfernt den ersten Fund von element.
liste8 = [3, 7, 23, 42]
liste8.remove(23)
print(liste8)      # [3, 7, 42]
# liste8.remove(23)  # ValueError: list.remove(x): x not in list

# extend(element)
# Erweitert die Liste am Ende um den INHALT von element
x = [1, 2, 3]
y = [7, 8, 9]
x.extend(y)
print(x)  # [1, 2, 3, 7, 8, 9]
x.extend("Hallo")
print(x)  # [1, 2, 3, 7, 8, 9, 'H', 'a', 'l', 'l', 'o']
a = [1, 2, 3]
b = [7, 8, 9]
a.append(b)
print(a)   # [1, 2, 3, [7, 8, 9]]

m = [1, 2, 3]
m.extend([4, 5, 6])
print(m)  # [1, 2, 3, 4, 5, 6]

# sort()
# Sortiert die Elemente der List aufsteigend
s = [23, 3, 42, 7, 11, 19]
s.sort()
print(s)  # [3, 7, 11, 19, 23, 42]
k = ["Keks", "Socke", "Opel", "Lobo"]
k.sort()
print(k)  # ['Keks', 'Lobo', 'Opel', 'Socke']

# clear() - Leert die Liste
s.clear()
print(s)  # []
































