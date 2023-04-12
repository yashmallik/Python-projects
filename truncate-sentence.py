def truncateSentence(self, s: str, k: int) -> str:
    news = s.split(" ")
    return " ".join(news[:k])
