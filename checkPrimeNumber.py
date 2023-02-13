def checkPrime():
    # Taking number from user
    number = int(input("Please Enter your number: "))
    # square root the number to decrease the time complexity and adding 2 for precaution check and range() function
    sqrtNum = int(number**.5)+2
    # using for loop for check every value of i, if number is divisible by i.
    for i in range(2,sqrtNum):
        if number%i==0:
            return print(f"{number} is not a prime number")
    return print(f"{number} is a Prime number")


checkPrime()