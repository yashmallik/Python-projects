try:
    nu = int(input("Please enter numerator: "))
    de = int(input("Please enter denominator: "))
    if de % nu == 0:
        print(nu, "is divisible by", de)
    else :
        print (nu, "is not divisible by", de)
except:
    print("Please enter integer value")



    
