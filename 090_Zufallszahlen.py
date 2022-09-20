
# Zufallszahlen

from random import randint
# Steht nicht automatisch zur Verfügung wie z.B. print()

wochentag = randint(1, 7)
print(wochentag)

if wochentag == 1:
    print("Montag")
elif wochentag == 2:
    print("Dienstag")
elif wochentag == 3:
    print("Mittwoch")
elif wochentag == 4:
    print("Donnerstag")
elif wochentag == 5:
    print("Freitag")
else:
    print("Wochenende")

# Würfel
wuerfel = randint(1, 6)
print("Du hast eine", wuerfel, "gewürfelt!")




