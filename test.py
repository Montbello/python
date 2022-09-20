
i = 0
z = 0
while i < 20:
    j = i
    while j < 20:
        z = z + j
        j = j +1
    i = i + 5
print(z)

"""
1 -> 0
2 -> -2
3 -> 600
4 -> 7
5 -> Endlosschleife
6 -> 95
"""

i = 10
z = 100
while i > 0:
    if i % 2 == 0:
        z = z - i
    else:
        z = z + i
    i = i - 1
print(z)





