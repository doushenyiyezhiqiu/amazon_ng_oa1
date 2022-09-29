def searchword_and_resultword(searchWord, resultWord):
    p1, p2 = 0, 0
    m, n = len(searchWord), len(resultWord)
    while p1<m and p2<n:
        if searchWord[p1] == resultWord[p2]:
            p1 += 1
            p2 += 1
        else:
            p1 += 1
    return n-p2

print(searchword_and_resultword('armaze', 'amazon'))