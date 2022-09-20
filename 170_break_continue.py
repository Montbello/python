
# break
# Kann nur in Schleifen auftauchen
# Beendet die Schleife direkt und komplett.

for i in range(10):
    print(i, end=" ")  # 0 1 2 3 4 5 6
    if i == 6:
        break
print()

zahl = 1
fak = 1
while True:
    fak = fak * zahl
    if fak >= 1_000_000_000:
        break
    print(fak, zahl)
    zahl += 1
# print(fak, zahl)

# continue
# Beendet den aktuellen Schleifendurchlauf vorzeitig
# und macht danach mit dem nächsten Durchlauf weiter.
# continue from top
for i in range(10):
    if i == 7:
        continue
    print(i, end=" ")  # 0 1 2 3 4 5 6 8 9
print()

# Alternative ohne continue
for i in range(10):
    if i != 7:
        print(i, end=" ")  # 0 1 2 3 4 5 6 8 9
print()


















