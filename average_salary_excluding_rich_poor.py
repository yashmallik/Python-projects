def average(self, salary: List[int]) -> float:
    high = max(salary)
    low = min(salary)
    return (sum(salary)-high-low)/(len(salary)-2)
