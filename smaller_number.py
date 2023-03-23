def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    sorted_nums = sorted(nums)
    mapping = dict()
    for i, n in enumerate(sorted_nums):
        if n not in mapping:
            mapping[n] = i

    return [mapping[key] for key in nums]
