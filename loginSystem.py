def loginSystem():
    # Create a list of username
    users = ["ram","shayam","sita","sam","gita","rita","mohan","john","mike"]
    # Create a dictionary with username and password
    pwd={"ram":"1234","shayam":"4689","sita":"5678","sam":"5432","gita":"1234@","rita":"1234!","mohan":"1234$","john":"1234%","mike":"987"}
    # Create a second dictionary for user's department
    dep={"ram":"student","shayam":"student","sita":"student","sam":"student","gita":"faculty","rita":"faculty","mohan":"faculty","john":"faculty","mike":"faculty"}
    # Taking username from the user and cleaning it
    user = input("Please enter your userid: ").strip().lower()
    # Checking for valid username
    if user in users:
        # Taking password for username from the user and cleaning it
        password = input("Please Enter your password: ").strip().lower()
        # Checking for valid password
        if password == pwd[user]:
            # Welcoming user with there department And captilising the user's first letter.
            print(f"Welcome! {user[0].upper()+user[1:]}, you are {dep[user]}")
        else:
            print("Wrong Password")
    else:
        print("Worng username")



loginSystem()
