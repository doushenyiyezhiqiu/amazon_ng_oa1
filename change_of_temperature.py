def change_of_temperature(tempChange):
    n = len(tempChange)
    right_left = [0]*n
    left_right = [0]*n
    ans = 0
    left_right[0] = tempChange[0]
    right_left[n-1] = tempChange[-1]
    for i in range(n-2, -1, -1):
        right_left[i] = right_left[i+1]+tempChange[i]
    for i in range(1,n):
        left_right[i] = left_right[i-1]+tempChange[i]
        ans = max(right_left[i], left_right[i])
    return ans

print(change_of_temperature([6,-2,5]))