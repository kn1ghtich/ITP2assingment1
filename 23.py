import math
#exercise 23.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = (2 * math.cos(x - math.pi / 6)) / (1/2 * math.sin(y) ** 2)
b = 1 + (z ** 2) / (3 + (z ** 2) / 5)

print("The value of a = " + str(a))
print("The value of b = " + str(b))
