
# exercise 2.

a = float(input("Enter the weight of rectangle: "))
b = float(input("Enter the height of rectangle: "))
if a % 1 == 0 and b % 1 == 0:
    a = int(a)
    b = int(b)
print("The perimeter of rectangle = " + str(2*(a+b)))
print("The area of rectangle = " + str(a*b))


