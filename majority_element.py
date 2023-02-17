def majorityElement(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    ele, count = 0, 0
    for i in sorted_nums:
        if i == ele:
            count += 1
        else:
            ele = i
            count = 1
        if count > (len(nums)//2):
            return ele


print(majorityElement([3, 1, 3]))
