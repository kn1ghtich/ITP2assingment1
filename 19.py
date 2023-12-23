import math
#exercise 19.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = (math.sqrt(abs(x-1)) - math.pow(abs(y), 1. / 3)) / (1 + (x**2)/2 + (y**2)/4)
b = x*(math.atan(z) + math.pow(math.e, -(x+3)))

print("The value of a = " + str(a))
print("The value of b = " + str(b))
