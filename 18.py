import math

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
arithmetic = (first + second) / 2

if arithmetic % 1 == 0:
    arithmetic = int(arithmetic)

geometric = math.sqrt(first*second)
if geometric % 1 == 0:
    geometric = int(geometric)

print(f"The arithmetic mean = {arithmetic}")
print(f"The geometric mean = {geometric}")
