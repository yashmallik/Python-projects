from functools import reduce


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signfunc = reduce(lambda x, y: x*y, nums)
        if signfunc > 0:
            return 1
        if signfunc < 0:
            return -1
        else:
            return 0


nums[-1, -2, -3, -4, 1, 2, 3]
obj = Solution()
print(obj.arraySign(nums))
