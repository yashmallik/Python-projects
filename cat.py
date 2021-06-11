fhand = open(input("Enter file name: "))
day = dict()
for line in fhand:
    words = line.split("")
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in day:
            day[words[2]] = 1
        else:
            day[words[2]] +=1
print(day)
print(day)
