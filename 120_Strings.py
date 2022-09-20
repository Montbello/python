
# String - Zeichenkette

str1 = "Hallo"

# Indexing mit eckigen Klammern []
# Um auf die einzelnen Zeichen zuzugreifen
# Null-basiert
print(str1[0])  # H
print(str1[1])  # a
print(str1[2])  # l
print(str1[3])  # l
print(str1[4])  # o

str2 = "12345"
print(str2[3])  # 4
print(str2[3], str2[4], sep="")  # 45

# Slicing per Teilbereichsoperator (:)
# string[start:ende]
# start ist inklusive, ende ist exklusive
str1 = "Hallo"
print(str1[2:4])  # ll
print(str1[0:4])  # Hall
str3 = "01234567"  # 012   345   67

print(str3[3:6])  # 345
print(str3[3], str3[4], str3[5])  # 3 4 5

# Wenn start 0 ist, kann der Wert weggelassen werden (0 ist Standard)
print(str1[:4])  # Hall

# Wenn ende fehlt, wird bis zum Ende geschnitten.
print(str1[1:])  # allo

# String-Operatoren
# Verkettung - Konkatenation (concatenation) mit +
x = "Hallo"
y = "Peter"
z = x + " " + y
print(z)  # Hallo Peter
print("Eins" + "Zwei" + "Drei" + "Viertel")
print("EinsZwei" + "Drei" + "Viertel")
print("EinsZweiDrei" + "Viertel")
print("EinsZweiDreiViertel")                  # EinsZweiDreiViertel
a = "Hund"
b = "Katze"
c = "Maus"
ausgabe = a + " frisst " + b + " frisst " + c
print(ausgabe)  # Hund frisst Katze frisst Maus

# String-Multiplikation mit *
# Einer der Operanden (Werte) muss ein String sein und der andere ein Integer
string1 = "Hello"
print(string1 * 7)  # HelloHelloHelloHelloHelloHelloHello
print((string1 + " ") * 7)  # Hello Hello Hello Hello Hello Hello Hello
print(3 * "Test")  # TestTestTest
























