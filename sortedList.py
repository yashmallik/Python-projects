name = input("Enter name:")
roll = int(input("Enter roll:"))
marks1 = int(input("Enter marks1:"))
marks2 = int(input("Enter marks1:"))
marks3 = int(input("Enter marks1:"))
average = (marks1+marks2+marks3)/3
if (marks1 >= 40) and (marks2 >= 40) and (marks3 >= 40):
    total = (marks1+marks2+marks3)
    if total > 260:
        print(f'{name} is first')
    elif total > 230:
        print(f'{name} is second')
    elif total > 190:
        print(f'{name} is third')
    else:
        print(f"{name} is promoted")

else:
    print(f"{name} is fail")
