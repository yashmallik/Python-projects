def subtractProductAndSum(self, n: int) -> int:
    mul = 1
    add = 0
    while n > 0:
        num = n % 10
        mul *= num
        add += num
        n = n//10
    diff = mul - add
    return diff
