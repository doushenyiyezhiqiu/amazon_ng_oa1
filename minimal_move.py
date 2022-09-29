def minimal_move(nums):
    one_pos = []
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            one_pos.append(i)
    # put all '1's to the tail
    m = len(one_pos)
    res1, res2 = 0, 0
    for i in range(len(one_pos)):
        res1 += n - m + i - one_pos[i]
    # put all '1's to the head
    for i in range(len(one_pos)):
        res2 += one_pos[i] - i
    return min(res1, res2)

print(minimal_move([0, 1, 1, 1, 1, 0, 1]))
