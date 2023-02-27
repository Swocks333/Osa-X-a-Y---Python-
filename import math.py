import math
aX=float(input("vloz hodnotu pro osu x bod a"))
bX=float(input("vloz hodnotu pro osu x bod b"))
aY=float(input("vloz hodnotu pro osu y bod a"))
bY=float(input("vloz hodnotu pro osu y bod b"))

cX= aX - bX
cY= aY - bY

cX=cX**2
cY=cY**2
cZ2=cX+cY
cZ=math.sqrt(cZ2)
print("konečná hodnota je výsledek ",cZ)