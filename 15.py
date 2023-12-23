# exercise 15.

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))
list = [a,b,c,d]
sum = 0
multiple = 1
for i in list:
    sum += i
    multiple *= i
print("Sum equal to " + str(sum))
print("Multiple equal to " + str(multiple))


"""
#or 

list = []
for i in range(4):
    list.append(int(input("Enter a number: ")))

for i in list:
    sum += i
    multiple *= i
print("Sum equal to " + str(sum))
print("Multiple equal to " + str(multiple))

"""