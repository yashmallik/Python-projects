def findArray(self, pref: List[int]) -> List[int]:
    arr, n = [pref[0]], len(pref)
    for i in range(1, n):
        arr.append(pref[i-1] ^ pref[i])
    return arr
