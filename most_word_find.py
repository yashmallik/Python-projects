def mostWordsFound(self, sentences: List[str]) -> int:
    max_len = 0
    for sentence in sentences:
        words = sentence.split(" ")
        max_len = max(max_len, len(words))
    return max_len
