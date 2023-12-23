import math
#exercise 20.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = (3 + math.pow(math.e, y-1)) / (1 + (x**2) * abs(y - math.tan(z)))
b = 1 + abs(y-x) + ((y-x) ** 2)/2 + (abs(y-x)**3)/3

print("The value of a = " + str(a))
print("The value of b = " + str(b))
