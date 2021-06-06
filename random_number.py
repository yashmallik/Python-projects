from random import randint
guess = randint(1,100)
real_guess = 0
check = 1
while guess != real_guess :
    print('guess chance number %d: ' % check, end="")
    try:
        real_guess = int(input("Enter your guess number: "))
    except :
        print("Please enter numeric value")
        exit()
    if real_guess < guess :
        print("Your guess is low")
    elif real_guess >guess :
        print("Your guess is too high")
    check += 1
print("your guess is correct")

