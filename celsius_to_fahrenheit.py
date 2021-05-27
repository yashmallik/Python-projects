try:
    c = float(input("Please enter your temperature in celsius: "))
    f = (c*(9/5))+32
    print("Your temperature in farenheit is:" ,str(f)+"F")
except:
    print("Please enter only numeric value")