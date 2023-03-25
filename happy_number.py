def isHappy(self, n: int) -> bool:
    nums = []
    while (True):
        n = str(n)
        b = 0
        for i in n:
            b += int(i)**2
        if b == 1:
            return True
        if b in nums:
            print(nums)
            return False
        nums.append(b)
        n = b
