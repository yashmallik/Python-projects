def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    l = []
    st = set(nums)
    for i in range(1, len(nums)+1):
        if i not in st:
            l.append(i)
    return l
