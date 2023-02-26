
def climbStairs(self, n: int) -> int:
    list_str = [0, 1, 2]
    for i in range(3, n+1):
        list_str.append(list_str[i-2] + list_str[i-1])
    return list_str[n]
