def find_a(string):
    count = 0
    for i in string.lower():
        if i == "a":
            count += 1
    return count


string = "programming is a fun game"
print(find_a(string))
