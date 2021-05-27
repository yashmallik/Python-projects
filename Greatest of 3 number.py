try :
    st = int(input("Please enter the first number: "))
    nd = int(input("Please enter the second number: "))
    rd = int(input("Please enter the third number: "))
    num = [st, nd, rd]
    print("The largest number is: ", max(num))
except :
    print("Please enter integer value")