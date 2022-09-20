
# Zuweisungsoperatoren - Assignment operator

x = 17

# Verkürzte Schreibweise: +=, ...
x = x + 1
print(x)  # 18
x += 1
print(x)  # 19
x -= 3    # entspricht: x = x - 3
print(x)  # 16
x *= 3
print(x)  # 48
x /= 4
print(x)  # 12.0
x %= 5
print(x)  # 2.0
x **= 7   # x = x ** 7
print(x)  # 128.0

# Inkrementoperator ++
# Gibt es in Python NICHT
# x++ erhöht um genau eins
"""
x += 1
x++
x--
"""

# Mehrere Variablen in einem Initialisieren
a = b = c = True
print(a, b, c)  # True True True
y, z = 3, 4













