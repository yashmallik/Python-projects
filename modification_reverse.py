def reverseString(s: list[str]) -> None:
    """
        Do not return anything, modify s in-place instead.
        """
    initial = 0
    final = len(s)-1
    while initial < final:
        s[initial], s[final] = s[final], s[initial]
        initial += 1
        final -= 1

# or
#   s.reverse()
