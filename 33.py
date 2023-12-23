import math

#exercise 33.
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
x3 = float(input('Enter x3: '))
y3 = float(input('Enter'))

p = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2) + math.sqrt((x3 - x1) ** 2 + (y3 -y1) ** 2)
print('The perimeter = '  + str(p))