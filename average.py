import re
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'short-mbox.txt'
try:
    fhand = open(fname)
except:
    print("invalid file name:")
    quit()

paper = list()
for lines in fhand:
    lines = lines.rstrip()
    n = re.findall('^New Revision:.* ([0-9.]+)', lines)
    if len(n) != 1: continue
    print(n)
    n = float(n[0])
    paper.append(n)

print(sum(paper)/len(paper))