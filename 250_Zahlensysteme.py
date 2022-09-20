
# Zahlensysteme

# Binär (b | B)
# Dual
print(0b10001)        # 17
print(type(0b10001))  # <class 'int'>
print(bin(17))        # 0b10001
print(type(bin(17)))  # <class 'str'>

print(0b0001)  # 1  <- 2 ** 0
print(0b0010)  # 2  <- 2 ** 1
print(0b0100)  # 4  <- 2 ** 2
print(0b1000)  # 8  <- 2 ** 3
print(0b0011)  # 3

print(0b11111111)  # 255
print(0b10000000)  # 128 <- 2 ** 7
print(0b01000000)  # 64  <- 2 ** 6
print(0b00100000)  # 32  <- 2 ** 5
print(0b00010000)  # 16  <- 2 ** 4

# Octal (o | O)
# Nur 0, 1, 2, 3, 4, 5, 6, 7 sind mögliche Ziffern im Oktalen-Zahlensystem
print(0o10)  # 8
print(oct(123456789))  # 0o726746425

# Hexadezimal (x | X)
# (A, B, C, D, E, F) | (a, b, c, d, e, f)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F sind mögliche "Ziffern" im Hexadezimalen-Zahlensystem
print(0x10)  # 16
print(0xFF)  # 255
print(type(0xFF))  # <class 'int'>
print(hex(255))    # 0xff

# Wieviel ist 0xCD als binäre Zahl?
print(bin(0xCD))  # 0b11001101
print(bin(0xC))  # 0b1100
print(bin(0xD))  # 0b1101

# Wieviel ist 0b10011010 als hexadezimale Zahl?
print(hex(0b10011010))  # 0x9a














