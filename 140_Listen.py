
# Listen
# Ein Datentyp
# In anderen Sprachen sind dies oft (nummerische) Arrays
# Eckige Klammern zum Erzeugen einer Liste
# Listen sind veränderbar (mutable)
# Listen sind null-basiert

liste1 = [3, 7, 23, 42]
print(liste1)  # [3, 7, 23, 42]
print(type(liste1))  # <class 'list'>

# Gemischte Datentypen in einer Liste sind in Python möglich
liste2 = [3, "Hello", 7.7, True]
print(liste2)  # [3, 'Hello', 7.7, True]

# Indexing
print(liste1[0])  # 3
print(liste1[1])  # 7
print(liste1[2])  # 23
print(liste1[3])  # 42

# Bestehende Liste verändern
liste1[0] = 77
print(liste1)  # [77, 7, 23, 42]

# Slicing - (in Scheiben schneiden)
# list1[start:ende]
# start inklusive, ende exklusive
liste1 = [3, 7, 23, 42]
print(liste1[1:3])  # [7, 23]

# Listen-Funktion list()
liste3 = list("Hallo")
print(liste3)  # ['H', 'a', 'l', 'l', 'o']

# list() mit range()
zahlen = list(range(1, 11))
print(zahlen)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# len() für length/Länge
print(len(zahlen))  # 10
















