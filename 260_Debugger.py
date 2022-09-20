
# Debugging mit dem Debugger

# breakpoint()
# Setzt einen Breakpoint als Alternative zu dem grafischen Breakpoint in PyCharm

x = 1
y = 2
z = 3

for i in range(10):
    x += 1
    y += x
    z += y

print(x, y, z)  # 11 67 298

