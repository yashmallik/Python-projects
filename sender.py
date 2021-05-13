fhand = open('mbox.txt')
names = list()
for lines in fhand:
    lines.rstrips()
    if lines.startwith('FROM'):
        key = lines[2]
        names.append(key)
    else:
        continue
print(names)
