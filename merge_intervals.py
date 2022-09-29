def merge_intervals(arrs):
    arrs.sort()
    ans = 0
    end = arrs[0][1]
    for i in range(1, len(arrs)):
        if arrs[i][0] < end:
            end = min(arrs[i][1], end)
            ans += 1
    return ans

print(merge_intervals([[1, 2], [2, 3], [3, 5], [4, 5]]))