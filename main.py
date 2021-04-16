import math

# this is a program to use the dimensions of a square to calculate the area of ​​a circle that fits inside


sidelength1 = 0
sidelength2= 0

print('Blockcrafter21,email:blockdevelopment@gmx.net, all rights reserved')
start = input('Press 5 to start')
start = float(start)

if start == 5:
    # hauptteil
    sidelength1 = input("Please enter the one side length")
    sidelength1 = float(sidelength1)
    sidelength2 = input("Please enter the other side length")
    sidelength2 = float(sidelength2)
    print(sidelength1)
    print(sidelength2)
    if sidelength1 < sidelength2:
        diameter = sidelength1
        radius = diameter / 2
        circulararea = math.pi * diameter ** 2
        print(f"{circulararea} is the area of the circle")

    else:
        diameter = sidelength2
        radius = diameter / 2
        circulararea = math.pi * radius ** 2
        print(f"{circulararea} is the area of the circle")
else:
    print('hey wait wrong number ')
