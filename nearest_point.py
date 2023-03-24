class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        small = 100000
        for i in range(len(points)):
            X = x-points[i][0]
            Y = y-points[i][1]
            if X*Y == 0 and abs(X+Y) < small:
                small = abs(X+Y)
                index = i
        return index


x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]


obj = Solution()
print(obj.nearestValidPoint(x, y, points))
