def diff(nums: list[int]):
    sumarr = []
    left = 0
    right = sum(nums)
    for num in nums:
        left += num
        sumarr.append(abs(left - right))
        right -= num
    return sumarr


nums = [10, 4, 8, 3]
print(diff(nums))
