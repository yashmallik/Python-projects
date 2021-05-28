x = int(input("Enter X coordinate point: "))
y = int(input("Enter Y coordinate point: "))

if x > 0 and y > 0 :
    print ("You are in First quadrant")
elif x < 0 and y > 0 :
    print ("You are in Second quadrant")
elif x < 0 and y < 0 :
    print ("You are in Third quadrant")
elif x > 0 and y < 0 :
    print ("You are in Fourth quadrant")
elif x == 0 and y == 0 :
    print ("You are at the point of origin")
elif x == 0 :
    print("You are at X point")
elif y == 0 :
    print ("You are at Y point")