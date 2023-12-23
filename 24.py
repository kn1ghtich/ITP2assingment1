import math
#exercise 24.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = (1 + math.sin(x+y) ** 2) / (2 + abs(x - 2*x / (1 + x*x*y*y)))
b = math.cos(math.atan(1/z)) ** 2

print("The value of a = " + str(a))
print("The value of b = " + str(b))
