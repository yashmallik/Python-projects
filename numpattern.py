def printTriangle(N):
    string = [str(i) for i in range(1, N+1)]
    revstring = string[::-1]
    # Code here
    for i in range(1, N+1):
        print(" ".join(string[:i]) + (" "*(10-(2*i))) +
              (" "*(10-(2*i)))+" ".join(revstring[N-i:]))


printTriangle(5)
