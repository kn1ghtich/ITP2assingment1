
# exercise 3.

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a % 1 == 0 and b % 1 == 0 and c % 1 == 0:
    a = int(a)
    b = int(b)
    c = int(c)
print("The V of the rectangular parallelepiped = " + str(a*b*c))
print("The S of the rectangular parallelepiped = " + str (2 * (a*b + b*c+ a*c)))

