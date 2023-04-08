def restoreString(s: str, indices: List[int]) -> str:
    a = [s[indices.index(i)] for i in range(len(indices))]
    return ''.join(a)
