# The algorithm I use is that if rating[i] is bigger or equal to rating[i-1]
# (the previous element), the count number will restart to count from 0, else count number
# plus 1.
# Time complexity: O(n), n is the length of the array 'rating'
# Space complexity: O(1)
import math


def continuous_decreasing_day(ratings):
    ans = 0
    cou = 1
    n = len(ratings)
    for i in range(1, n):
        if ratings[i] == ratings[i-1] + 1:
            cou += 1
        else:
            ans += (cou + 1) * cou // 2
            cou = 1
    ans += (cou + 1) * cou // 2
    return ans

print(continuous_decreasing_day([4, 3, 5, 4, 3]))



def oa1(packets, channels):
    packets.sort(reverse = True)
    ans = 0
    i = 0
    while i < channels - 1:
        ans += packets[0]
        packets.remove(packets[0])
        i += 1
    n = len(packets)
    if n == 0:
        return ans
    if n % 2 == 0:
        ans += ((packets[i//2] + packets[i//2 - 1])/2)
    else:
        ans += packets[i//2]
    return math.ceil(ans)

print(oa1([1,2,3,5,4],3))