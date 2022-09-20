
# while
# Solange

# while als Zählschleife
# Die Schleife so oft durchlaufen, wie die Bedingung True ist.
i = 1
while i < 6:
    print(i, end=" ")  # 1 2 3 4 5
    # i += 1
    i = i + 1
print("\n---")

# Das Gleiche als for-Schleife:
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print("\n---")


# Das Programm ermittelt wie oft gewürfelt wird, bis eine sechs kommt.
from random import randint
w = randint(1, 6)
c = 1
print(w, end=" ")
while w != 6:
    c += 1
    w = randint(1, 6)
    print(w, end=" ")
print("Anzahl:", c)































