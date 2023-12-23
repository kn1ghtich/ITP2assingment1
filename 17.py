
# exercise 17

edge = float(input("Enter an edge length of a cube: "))
volume = edge ** 3
sideArea = edge ** 2
if volume % 1 == 0:
    volume = int(volume)
if sideArea % 1 == 0:
    sideArea = int(sideArea)
print("The volume of the cube: " + str(volume))
print("The side area of the cube: " + str(sideArea))
