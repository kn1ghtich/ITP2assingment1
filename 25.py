import math
#exercise 25.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = math.log( abs((y - math.sqrt(abs(x)))   *   (x - y/(z + (x*x)/ 4))))
b = x - (x**3) / math.factorial(3) + (x**5) / math.factorial(5)

print("The value of a = " + str(a))
print("The value of b = " + str(b))
