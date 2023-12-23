import math
#exercise 21.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = (1+y) * ((x+y/ ((x**2) + 4)) / (math.e ** (-x-2) + 1/((x**2) + 4)))
b = (1 + math.cos(y-2)) / ((x ** 4) / 2 + math.sin(z) ** 2)

print("The value of a = " + str(a))
print("The value of b = " + str(b))
