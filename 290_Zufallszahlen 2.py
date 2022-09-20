
# Zufallszahlen 2

# uniform
# Gibt einen zufälligen Float zurück
from random import uniform
print(uniform(1, 130))  # z.B. 107.47604248871536

# random
# Gibt eine Zahl zwischen 0 - 0.9999999 zurück
from random import random
print(random())  # 0.7176642274968313
print(random())               # 0 - 0.9999999
print(random() * 6)           # 0 - 5.9999999
print(int(random() * 6))      # 0 - 5
print(int(random() * 6) + 1)  # 1 - 6

# gauss
# Aus der Statistik
# Benannt nach dem Mathematiker/Statistiker Carl-Friedrich Gauss
# Normalverteilung - Glockenkurve - Gauss'sche Glocke
from random import gauss
mu = 100    # Erwartungswert
sigma = 50  # Standardabweichung
print(gauss(mu, sigma))  # 117.9873294517951

# Konsole: pip install matplotlib
from random import gauss
import matplotlib.pyplot as pyplot

nums = []
mu = 100
sigma = 50

for i in range(10000):
    temp = gauss(mu, sigma)
    nums.append(temp)

pyplot.hist(nums, bins=200)
pyplot.show()









