
# Datum & Zeit

from datetime import datetime

# now()-Methode
# ISO 8601 Format
jetzt = datetime.now()
print(jetzt)  # 2022-05-12 11:40:08.548523

# datetime()-Methode
# Konstruktor der Datetime-Klasse
geburtstag = datetime(1970, 12, 3, 9, 35, 0)
print(geburtstag)  # 1970-12-03 09:35:00

# time()
# Zeit
print(jetzt.time())  # 11:47:57.140794

# Timestamp, der UNIX-Zeit
# Sekunden seit 01.01.1970
# 32-Bit-Integer -> 2.100.000.000
print(jetzt.timestamp())  # 1_652_348_967.692146
print(geburtstag.timestamp())  # 29_061_300.0

print(jetzt.timestamp() - geburtstag.timestamp())  # 1623288304.395351


