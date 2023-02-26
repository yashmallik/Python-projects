string = input("Enter your string: ")
string_array = [*string]
string_set = set(string_array)

print(True) if len(string_array) % len(string_set) == 1 else print(False)
print(string_array)
