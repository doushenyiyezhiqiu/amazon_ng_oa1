def subsequence_of_AZ(s):
    n = len(s)
    new1 = list(s) + ['Z']
    new2 = ['A'] + list(s)
    res1, res2 = 0, 0
    pre_A = 0
    for i in range(n+1):
        if new1[i] == 'A':
            pre_A += 1
        if new1[i] == 'Z':
            res1 += pre_A

    pre_A = 0
    for i in range(n+1):
        if new2[i] == 'A':
            pre_A += 1
        if new2[i] == 'Z':
            res2 += pre_A

    return max(res1, res2)

print(subsequence_of_AZ('BAZAZ'))
print(subsequence_of_AZ('A'))