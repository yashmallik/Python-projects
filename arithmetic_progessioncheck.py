
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        check = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if check != arr[i]-arr[i-1]:
                return False
        return True


arr = [3, 5, 1]
obj = Solution()
print(obj.canMakeArithmeticProgression(arr))
