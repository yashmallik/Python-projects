try:
    f = float(input("Enter your farenheit temperature: "))
    c = round((f-32)*(5/9))
    print("Here is you temperature in celsius:", str(c)+"C")
except:
    print("Please enter only numeric value")