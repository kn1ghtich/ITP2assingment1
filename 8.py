
# exercise 8.

x = float(input("Enter x = "))
y = 3*(x**6) - 6*(x*2) + 7
if y % 1 == 0:
    y = int(y)
print("y = " + str(y))
