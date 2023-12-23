# exercise 9.

x = float(input("Enter x = "))
y = 4*((x-3)**6) + 7*((x-2)**3) + 2
if y % 1 == 0:
    y = int(y)
print("y = " + str(y))
