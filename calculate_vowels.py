def vowels(strings):
    count = 0
    vowel = ["a", "e", "i", "o", "u"]
    for i in strings.lower():
        if i in vowel:
            count += 1
    return count


string = "I love Coding"
print(vowels(string))
