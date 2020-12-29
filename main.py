import math

# this is a program to use the dimensions of a square to calculate the area of ​​a circle that fits inside


sidelength1 = 0
sidelength2= 0

print('Blockcrafter21,email:blockdevelopment@gmx.net, all rights reserved')
start = input('Press 5 to start')

if start == 5:
    # hauptteil
    sidelength1 = input("Bitte die eine Seitenlaenge eingeben")
    sidelength1 = float(seitenlaenge1)
    sidelength2 = input("Bitte die andere Seitenlaenge eingeben")
    sidelength2 = float(seitenlaenge2)
    print(sidelength1)
    print(sidelength2)
    if sidelength1 < sidelength2:
        diameter = sidelength1
        radius = diameter / 2
        circulararea = math.pi * diameter
        print(f"die Fläche des Kreises ist{circulararea}")

    else:
        diameter = sidelength2
        radius = diameter / 2
        circulararea = math.pi * radius ** 2
        print(f"die fläche des kreises ist{circulararea}")
else:
    print('hey wait')
