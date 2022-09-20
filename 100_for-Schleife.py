
# for-Schleife und range()

# Zählschleife
# i als Variable ist Programmier-Richlinie

# Sonst: for (i = 0; i < 10, i++)

# range(ende)
# start ist 0
# ende ist exclusive
for i in range(10):
    print("Hello", end=" ")  # Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello
print()

for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

print("Hello", end="\n")
print("Hello")

# range(start, ende)
# start ist inklusive
# ende ist exclusive
for i in range(5, 10):
    print(i, end=" ")  # 5 6 7 8 9
print()

# range(start, ende, schrittweite)
# Schrittweite
# start ist inklusive
# ende ist exclusive
for i in range(1, 20, 3):
    print(i, end=" ")  # 1 4 7 10 13 16 19
print()

# Negative Schrittweite
# Hierbei muss start > ende sein
# start ist inklusive
# ende ist exclusive
for i in range(40, 20, -2):
    print(i, end=" ")  # 40 38 36 34 32 30 28 26 24 22
print()

# _ als Variable
for _ in range(10):
    print("Hello", end=" ")  # Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello
print()














