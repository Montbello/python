
# Runden

# round()
# Python rundet bei .5 zur geraden Zahl
#
# Als einzige populäre Programmiersprache
# Mathematisch Runden
print(round(3.49))     # 3
print(round(3.5))      # 4
print(round(4.5))      # 4
print(round(4.5001))   # 5
print(round(5.5))      # 6
print(round(6.5))      # 6
print(round(7.5))      # 8
print(round(8.5))      # 8

# "Alle" anderen runden kaufmännisch:
# .5 wird immer aufgerundet

# round() mit zweitem Parameter
# Der zweite Parameter gibt die Stellen hinter dem Komma an.
print(round(4.49, 0))      # 4.0 (.0, weil es ein Float ist)
print(round(4.449, 1))     # 4.4
print(round(4.449*10)/10)  # 4.4
print(round(4.45001, 1))   # 4.5
print(round(4.845001, 2))  # 4.85

import math
# ceil() zum Aufrunden zum höheren Integer
print(math.ceil(9.1))  # 10

# floor() zum Abrunden zum niedrigeren Integer
print(math.floor(9.7))  # 9

# Rundungsfehler bei Floats
print(1.1 + 2.2)  # 3.3000000000000003
print(round(1.1 + 2.2, 1))  # 3.3

# Abschließende Nullen fallen weg
x = 3.3000000
print(x)  # 3.3
# y = 007  # Führende Nullen gehen gar nicht in Python








