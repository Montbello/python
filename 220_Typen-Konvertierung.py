
# Typen-Konvertierung
# Type-Casting

# Explizite (ausdrückliche) Typen-Umwandlung

# str()
# print("Hello" + 42)     # TypeError: can only concatenate str (not "int") to str
print("Hello" + str(42))  # Hello42
print("Hello" + "42")     # Hello42

zahl = 77
ausgabe = "Meine Ausgabe: "
ausgabe += str(zahl)

# int()
# zahl = input("Bitte eine Zahl eingeben!")  # input() gibt einen String zurück
zahl = 23  # Simulierte Eingabe
# ergebnis = zahl + 42  # TypeError: can only concatenate str (not "int") to str
ergebnis = int(zahl) + 42
print(ergebnis)

print(int(123.999))  # 123 (die Kommastellen werden abgeschnitten)
print(int(True))     # 1
print(int(False))    # 0

# float()
# Aus einem String einen Float machen:
# eingabe = input("Bitte einen Float mit Punkt eingeben!")
eingabe = "123.4"  # Simulierte Eingabe
x = float(eingabe)
y = x + 100.0
print(y)  # 223.4

# Implizite Typen-Umwandlung
# Python kümmert sich selber um die Typen-Konvertierung:
print(True + True + False)  # 2









