try:

    num = int(input("Enter your digit"))
    sum = 0
    product = 1
    while num != 0:
        digit = x%10
        sum += digit
        product *= digit
        x //= 10
    print("Sum of your digit is: ",sum)
    print("Product of your digit is: ",product)
except:
    print("Invalid input")        
