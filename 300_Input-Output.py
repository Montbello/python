
# Input-Output
# Eingabe-Ausgabe
# Dateibehandlung - Filehandling

# open()
# Datei zum Schreiben öffnen (mit dem Modus "w" für write)
# Wenn die Datei nicht existiert, wird sie erstellt.
data = open("daten.txt", "w")

# Den Modus auslesen
print(data.mode)  # w

# Daten in die Datei schreiben
data.write("Zeile 1\n")
data.write("Hallo\n")
data.write("Welt\n")

# Datei schließen
data.close()

# Datei zum Lesen öffnen
# Der Modus "r" ist Standard und kann weggelassen werden.
# data = open("daten.txt", "r")
data = open("daten.txt")

# read() liest die ganze Datei aus
print(data.read())
print(data.read())

# seek()
# Den Dateizeiger an den Anfang zurück setzen
data.seek(0)
print(data.read())

# readline() liest die nächste Zeile aus
data.seek(0)
print(data.readline())
print(data.readline())

# readlines() gibt alle Zeilen als Liste zurück
data.seek(0)
print(data.readlines())  # ['Zeile 1\n', 'Hallo\n', 'Welt\n']













