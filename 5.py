# exercise 5.
import math

a = float(input("Enter cathet a: "))
b = float(input("Enter cathet b: "))
c = math.sqrt(a*a + b*b)
if a % 1 == 0 and b % 1 == 0 and c % 1 == 0 :
    a = int(a)
    b = int(b)
    c = int(c)
    p = a + b + c

print("The perimeter of triangle = " + str(p))
print("The cathet c of triange = " + str(c))
