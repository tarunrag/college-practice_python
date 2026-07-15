print("FIND AREA & VOLUME OF CYLINDER\n")

print("Enter Dimensions of Cylinder...")
rd = eval(input("Radius: "))
hg = eval(input("Height: "))
print()

import math

ar = 2*math.pi*rd*(rd+hg)
vl = math.pi*rd**2*hg

print("Area  :", ar)
print("Volume:", vl)
      
print()
ar = 2*3.14*rd*(rd+hg)
vl = 3.14*rd**2*hg
print("Area  :", ar)
print("Volume:", vl)

print()
ar = 2*22/7*rd*(rd+hg)
vl = 22/7*rd**2*hg
print("Area  :", ar)
print("Volume:", vl)
