def wheel(wheels):
    n = len(wheels)
    ans = [0]*n
    for i in range(n):
        if wheels[i]%2 == 0:
            ans[i] = wheels[i]//4 + 1
    return ans

print(wheel([4, 5, 6]))