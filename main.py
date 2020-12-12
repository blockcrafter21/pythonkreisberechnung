import math

# das ist ein programm um mit den Maßen eines Quadrats die fläche eines kreises zu berechnen der hinein passt


seitenlaenge1 = 0
seitenlaenge2 = 0

print('Blockcrafter21,email:blockdevelopment@gmx.net, all rights reserved')

# hauptteil
seitenlaenge1 = input("Bitte die eine Seitenlaenge eingeben")
seitenlaenge1 = float(seitenlaenge1)
seitenlaenge2 = input("Bitte die andere Seitenlaenge eingeben")
seitenlaenge2 = float(seitenlaenge2)
print(seitenlaenge1)
print(seitenlaenge2)
if seitenlaenge1 < seitenlaenge2:
    durchmesser = seitenlaenge1
    radius = durchmesser / 2
    flaechedeskreises = math.pi * durchmesser
    print(f"die Fläche des Kreises ist{flaechedeskreises}")

else:
    durchmesser = seitenlänge2
    radius = durchmesser / 2
    flaechedeskreises = math.pi * radius ** 2
    print(f"die fläche des kreises ist{flaechedeskreises}")


