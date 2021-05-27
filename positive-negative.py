try:
    a = int(input("Please enter the number: "))    
    if a < 0 :
        print ("Negative")
    else :
        print("Positive")
except:
    print("Please enter only numberic value")