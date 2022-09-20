
# Logische Operatoren
# Boolesche Opatoren

# and - or - not

# and
wochentag = "Samstag"
regen_status = "Kein Regen"
if wochentag == "Samstag" and regen_status == "Kein Regen":
    print("Super, so soll es sein!")
else:
    print("Na, toll!")

# Macht das Gleiche, aber ohne and
if wochentag == "Samstag":
    if regen_status == "Kein Regen":
        print("Super, so soll es sein!")
    else:
        print("Na, toll!")
else:
    print("Na, toll!")

# and ist nur True, wenn beide Seiten/Bedingungen True sind
# Sobald mindestens eine Seite False ist, ist das Gesamtergebnis False
print(True and True)    # True
print(False and True)   # False
print(True and False)   # False
print(False and False)  # False


# or
wochentag = "Donnerstag"
regen_status = "Kein Regen"
if wochentag == "Samstag" or regen_status == "Kein Regen":
    print("Ich bin schon happy. Eins reicht mir.")

# or ist True, sobald mindestens eine Seite True ist
print(True or True)
print(False or True)
print(True or False)
print(False or False)

# not
wochentag = "Donnerstag"
if not (wochentag == "Samstag"):  # equal to operator
# if not False:
    print("Schade, es ist leider nicht Samstag.")
if wochentag != "Samstag":  # not equal to operator
    print("Schade, es ist leider nicht Samstag.")

print(not True)   # False
print(not False)  # True















