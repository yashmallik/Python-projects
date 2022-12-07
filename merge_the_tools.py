"""Consider the following:

A string, s, of length n where s=c1,c2,c3,c.....
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, t, consists of a contiguous block of k characters in k. Then, use each t to create string u such that:

The characters in u are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in u occurs exactly once. In other words, if the character at some index j in t occurs at a previous index <j in t, then do not include the character in string u."""

def merge_the_tools(string, k):
    n = len(string)
    part = n//k
    count = 0
    while 0<part:
        substring = ""
        line = string[count*k:k*(count+1)]
        while len(line)>0:
            substring += line[0]
            line = line.replace(line[0],"")
        print(substring)
        part -= 1
        count += 1
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
