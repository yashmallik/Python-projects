def maximumWealth(self, accounts: List[List[int]]) -> int:
    rich = 0
    for i in accounts:
        i = sum(i)
        if i > rich:
            rich = i
    return rich
