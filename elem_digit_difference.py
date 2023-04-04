def differenceOfSum(self, nums: List[int]) -> int:
    arr = []
    elem_sum = sum(nums)
    digi_sum = 0
    diff = 0
    for i in nums:
        if i < 10:
            digi_sum += i
        else:
            i = str(i)
            arr = arr + [*i]
    arr = [int(i) for i in arr]
    digi_sum += sum(arr)
    return (abs(elem_sum - digi_sum))
