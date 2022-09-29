# First remember the position of zero, and then use a slide window to calculate the
# maximum length of consecutive ones
# Time complexity: O(n), n is the length of arr
# Space complexity: O(n), n is the length of zero_pos

def maximum_consecutive_ones(arr, m):
    n = len(arr)
    zero_pos = []
    for i in range(n):
        if arr[i] == 0:
            zero_pos.append(i)
    if len(zero_pos) <= m:
        return zero_pos
    right, left = m, -1
    max_val = zero_pos[right] - m
    ans = zero_pos[:m]
    while right < len(zero_pos):
        if left != -1:
            if max_val < zero_pos[right] - zero_pos[left] - 1 - m:
                ans = zero_pos[left+1:right]
        right += 1
        left += 1
    if max_val < n-zero_pos[left]-m:
        ans = zero_pos[left+1:]
    return ans

print(maximum_consecutive_ones([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 2))
print(maximum_consecutive_ones([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 1))
print(maximum_consecutive_ones([0, 0, 0, 1], 4))