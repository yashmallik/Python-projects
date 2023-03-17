def validMountainArray(self, arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    peak = arr.index(max(arr))
    if peak == len(arr)-1 or peak == 0:
        return False
    for i in range(1, peak):
        if arr[i-1] >= arr[i]:
            return False
    for j in range(peak, len(arr)-1):
        if arr[j] <= arr[j+1]:
            return False
    return True
