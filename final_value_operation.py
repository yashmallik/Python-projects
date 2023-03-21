def finalValueAfterOperations(self, operations: List[str]) -> int:
    sum = 0
    for i in operations:
        if i == 'X++' or i == '++X':
            sum += 1
        elif i == 'X--' or i == '--X':
            sum -= 1
    return sum
