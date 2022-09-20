
# Python-eigene Funktionen
# Built-in Functions

builtins = dir(__builtins__)
# print(builtins)

c = 0
for i in builtins:
    if i[0].islower():
        print(i, end=" ")
        # print(c, i, sep="", end=" ")
        c += 1
        if c % 20 == 0:      # Für die Zeilenumbrüche
            # if c in [20, 42, 65]:
            print()
print()
print(c)  # 75
