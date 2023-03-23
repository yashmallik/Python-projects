def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    limit = max(candies)
    result = []
    for candy in candies:
        if candy + extraCandies < limit:
            result.append(False)
        else:
            result.append(True)
    return result
