from math import sqrt
x = float(input("Insert X: "))
y = float(input("Insert Y: "))
z = float(input("insert Z: "))
a = y*y-4*x*z

if(a==0) :
    x1 = -y/2*x
    print("x1 = %.2f" %x1)
elif (a>0) :
    x1 = (-y + sqrt(a))/2*x
    x2 = (-y - sqrt(a))/2*x
    print("x1 = %.2f; x2 = %.2f" %(x2,x2))
else :
    print("there is no real root")