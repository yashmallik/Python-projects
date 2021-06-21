num1 = int(input("Enter your number: "))
base = int(input("Enter your base number (2 to 9): "))
if  not 2>= base <=9 :
    quit()
num2 = ""
while num1 > 0:
    num2 = str(num1 % base) + num2
    num1 //= base

print (num2)