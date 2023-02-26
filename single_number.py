def singleNumber(self, nums: List[int]) -> int:
    i = 0
    while nums:
        name = nums.pop(i)
        if name not in nums:
            return name
        else:
            nums.remove(name)
    return
