
# String-Methoden

s = "abcdefghijklmnopqrstuvwxyz"

print(s.upper())  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print("Hello".lower())  # hello
# capitalize() macht den ersten Buchstaben groß und den Rest klein:
print("hello World".capitalize())  # Hello world

# Methoden zum Testen
# Geben alle einen Boolean zurück

print(s.startswith("b"))   # False
print(s.endswith("z"))     # True

# isalpha() - testet, ob alles Buchstaben sind
print("Hello".isalpha())        # True
print("test123test".isalpha())  # False

# isdigit() - testet, ob alles Ziffern sind
print("1234".isdigit())   # True
zahl = int("1234")
print("123go".isdigit())  # False
# zahl2 = int("123go")  # ValueError

# isalnum() - testet, ob alles Buchstaben oder Ziffern sind
print("123Hello".isalnum())     # True
print("123Hello!!!".isalnum())  # False

# islower() - Testet, ob alle vorhandenen Buchstaben kleingeschrieben sind
# isupper() - Testet, ob alle vorhandenen Buchstaben großgeschrieben sind
print("abc123__!!".islower())  # True

# join(str)
# Setzt die Zeichenkette zwischen jedes Element der übergebenen Sequenz
s = "abcdefghijklmnopqrstuvwxyz"
print("-".join(s))  # a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z
print("-".join(["P", "W", "D"]))  # P-W-D
print("".join(["P", "W", "D"]))  # PWD
print(", ".join(["Hund", "Katze", "Maus"]))  # Hund, Katze, Maus
# In anderen Sprachen meistens anders rum: ["Hund", "Katze", "Maus"].join(", ")

# strip([str]) - zum Trimmen (dem Entfernen von Whitespace)
# str ist standardmäßig ein Leerzeichen
# Whitespace wird nur an den jeweiligen Enden des Strings entfernt.
print("---" + "       Hello World     ".strip() + "---")  # ---Hello World---
print("aabababaa".strip("a"))  # bbb
print("aabababaa".lstrip("a"))  # bbbaaa
print("aabababaa".rstrip("a"))  # aaabbb

# split([sep]) - teilt am Separator und erzeugt eine Liste
# sep ist standardmäßig ein Leerzeichen
print("Paul findet Python toll".split())  # ['Paul', 'findet', 'Python', 'toll']

# count(str) - zählt die Vorkommnisse eines übergebenen Strings
# Es gibt eine gleichnamige Listen-Methoden
print("ASDASDSAASDDSSASADS".count("s"))  # 0
print("ASDASDSAASDDSSASADS".count("S"))  # 8

# len() - Build-in-Funktion von Python, die mit allen Sequenzen funktioniert.
print(len("Hello Wolrd"))  # 11




