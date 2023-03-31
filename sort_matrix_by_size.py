def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    enu = enumerate(groupSizes)
    enu = sorted(enu, key=lambda x: x[1])
    cur = 0
    output = []
    for i, j in enu:
        if j == cur and len(output[-1]) < cur:
            output[-1].append(i)
        else:
            output.append([i])
            cur = j
        return output
