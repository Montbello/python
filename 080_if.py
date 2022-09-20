
# if
# WENN: Etwas wird ausgeführt oder nicht ausgeführt
# Die Bedingung wird durch einen Doppelpunkt beendet.
# Alles Folgende, was eingerückt ist, ist noch im if.

tag = 'Samstag'
# tag = "Montag"
if tag == "Samstag":
    print("Schönes Wochenende")  # Schönes Wochenende
    print("Weiterhin im if.")
print("Nicht mehr im if. Wird bedingungslos, in jedem Fall ausgeführt.")

"""
# In anderen Sprachen (Java, PHP, JS):
if (tag == "Samstag") {  
}
"""

# if else
# WENN ... SONST
# Genau einer der Zweige/Fälle wird in jedem Fall ausgeführt
# tag = "Freitag"
if tag == "Samstag":
    print("Schönes Wochenende")
else:
    print("Gute Woche")
print("Es ist bald Sommer.")  # Ist nicht mehr im else und wird immer ausgeführt.

"""
Hier kann ich
längere Notizen schreiben.
"""

# if elif else
# Es kann nur ein if und nur ein else geben, aber "beliebig" viele elif
# Es wird genau EINER der Fälle ausgeführt.
gehalt = 20000
steuersatz = 0

if gehalt < 10000:
    steuersatz = 0
elif gehalt < 30000:
    steuersatz = 0.2
elif gehalt < 100000:
    steuersatz = 0.35
else:
    steuersatz = 0.45

print("Steuern:", gehalt * steuersatz)  # Steuern: 4000.0

# if elif
zahl = 7
if zahl == 8:
    print("Test")
elif zahl == 9:
    print("Test2")











