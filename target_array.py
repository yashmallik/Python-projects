class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for i, j in zip(nums, index):
            target.insert(j, i)
        return target


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
obj = Solution()
print(obj.createTargetArray(nums, index))
