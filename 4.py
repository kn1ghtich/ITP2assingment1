# exercise 4.
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
gmean = math.sqrt(a*b)
if gmean % 1 == 0:
    gmean = int(gmean)
print("The geometric mean = " + str(gmean))

