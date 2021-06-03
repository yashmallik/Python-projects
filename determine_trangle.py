import sys
print ("Insert the lenght of your trangle")
while True :
    try :
        a = float(input("Enter the lenght of first side: "))
        b = float(input("Enter the length of second side: "))
        c = float(input("Enter the length of third side: "))

        if a+b>c and a+c>b and c+b>a :
            print ("This trangle exists")
            break
        else :
            print ("This trangle does not exists")
            break
    except :
        print ("Please enter numeric value")
        continue
