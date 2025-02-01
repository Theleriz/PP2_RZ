def uniq(lst:list) -> list:
    answerList = []
    for i in lst:
        if not (i in answerList):
            answerList.append(i)
    return answerList

