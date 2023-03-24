class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return (nums[i] + nums[i+1] + nums[i+2])
        return 0


nums = [2, 1, 2]
obj = Solution()
print(obj.largestPerimeter(nums))
