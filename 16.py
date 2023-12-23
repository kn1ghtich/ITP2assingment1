# exercise 16.

x = float(input("Enter x: "))
y = float(input("Enter y: "))

res = (abs(x) + abs(y)) / (1 + abs(x*y))
print("The result = " + str(res))
