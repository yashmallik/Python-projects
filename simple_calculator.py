print("Opening calculator...."+"....")
print("loading program---------")
print("Zero operation terminate the program!")
print('________________________________________________________')
while True :
    
    opert = input("Choose operator(+, -, *, /): ")
    if opert == 0:
        break
    if opert in ('+','-','*','/'):
        x = float(input("Enter your first number: "))
        y = float(input(str(x)+" "+str(opert) +" (Enter your last number): "))
        if opert == "+":
            print("%.2f" % (x+y))
        elif opert == "-" :
            print("%.2f" % (x-y))
        elif opert == "*":
            print ("%.2f" % (x*y))
        elif opert == "/":
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Error! Cannot divided by zero")
        else:
            print("invalid operator!")