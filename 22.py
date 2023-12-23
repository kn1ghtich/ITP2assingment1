import math
#exercise 22.

x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = y + (x / (y**2 + abs(x**2 / (y + x**3 / 3))))
b = (1 + math.tan(z/2) ** 2)

print("The value of a = " + str(a))
print("The value of b = " + str(b))
