try:
    leap = int(input("Please enter your year to check leap year: "))
    if leap % 4 == 0 and (leap % 100 != 0 or leap % 400 == 0) :
        print("This is a leap year")
    else :
        print ("This is not a leap year")
except:
    print("Please enter numeric value")