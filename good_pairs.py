def numIdenticalPairs(self, nums: List[int]) -> int:
    pair = 0
    dictnum = dict()
    for i in nums:
        if i in dictnum:
            dictnum[i] += 1
        else:
            dictnum[i] = 1
    for j in dictnum.values():
        pair += j*(j-1)//2
    return pair
