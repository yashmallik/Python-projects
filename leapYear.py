def leapYear():
# Taking input from user
    year = int(input("Please enter year you want to check: "))
    # checking coondition for leap year 
    # If year is divisible by 4 and not divisible by 100 or divisib
    if (year%4 == 0 and (year%100 !=0 or year%400 == 0 )):
        return print(f"{year} is a leap year")
    else:
        return print(f"{year} is not a leap year")

leapYear()