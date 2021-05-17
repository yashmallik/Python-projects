mhand = input('ENTER FILE NAME : ')
fhand = open(mhand)
names = list()
count = 0
for lines in fhand:
    word = lines.split()
    if words[0] !== ('FROM'): continue
    count = count + 1
    print(word[2])


    names.append(words[2])
print(names)
print("There are"),count,("people send message")
