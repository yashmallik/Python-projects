def check_palidrome(string):
    last = 1
    count = 0
    for i in string:
        if i == string[-last]:
            count += 1
        else:
            return False
        last += 1
    if count == len(string):
        return True


print(check_palidrome("civic"))

print(check_palidrome("palidrome"))
