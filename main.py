import math


seitenlänge1=0
seitenlänge2=0

#hauptteil
seitenlänge1= input("Bitte die eine seitenlänge eigeben")
seitenlänge1=float(seitenlänge1)
seitenlänge2= input("Bitte die andere seitenlänge eingeben")
seitenlänge2=float(seitenlänge2)
print(seitenlänge1)
print(seitenlänge2)
if seitenlänge1 < seitenlänge2:
    durchmesser=seitenlänge1
    radius = durchmesser / 2
    flächedeskreises = math.pi * durchmesser
    print(f"die fläche des kreises ist{flächedeskreises}")



else:
    durchmesser=seitenlänge2
    radius = durchmesser / 2
    flächedeskreises = math.pi * radius**2
    print(f"die fläche des kreises ist{flächedeskreises}")
print("test")

