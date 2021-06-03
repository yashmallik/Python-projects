import math
x = float(input("Insert point X: "))
y = float(input("Insert point Y: "))
r = float(input("Insert the radius: "))
hyp = math.sqrt(pow(x,2) + pow(y,2))
if hyp <= r :
    print("The point belongs to circle")
else :
    print("This point does not belong to circle")
