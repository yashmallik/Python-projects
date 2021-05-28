try :
    cal = input("Please choose the unit (m, v, d): ")

    if cal == "m" :
        v = float(input("volumn: "))
        d = float(input("Density: "))
        result = d*v
    elif cal == "v" :
        m = float(input("Mass: "))
        d = float(input("Density: "))
        result = m/d
    elif cal == "d"  :
        m = float(input("Mass: "))
        v = float(input("Volumn: "))
        result = m/v
    print("%.2f" % result)
except : 
    print ("Please enter correct value")