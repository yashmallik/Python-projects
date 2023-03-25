def areAlmostEqual(self, s1: str, s2: str) -> bool:
    arr = []
    index = []
    if s1 == s2:
        return True
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            arr.append(s1[i])
            index.append(i)
        if len(arr) > 2:
            return False
    if len(arr) == 2:
        if s2[index[0]] == arr[1] and s2[index[1]] == arr[0]:
            return True
    return False
