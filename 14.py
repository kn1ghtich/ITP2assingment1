# exercise 14.

a = float(input("Enter number a "))
b = float(input("Enter number b "))
c = float(input("Enter number c "))

list = []
list = sorted(list)
print("Sorted list " + str(list))


"""
# or
list = []
for i in range(3):
    list.append(int(input("Enter a number: ")))
list = sorted(list)
print("Sorted list " + str(list))

# or 
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("Sorted values by increasing", a, b, c)
"""