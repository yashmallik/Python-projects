def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
    mep = list(zip(*score))
     sort = sorted(list(mep[k]), reverse=True)
      sortscore = []

       for i in range(len(score)):
            n = mep[k].index(sort[i])
            sortscore.append(score[n])

        return sortscore
