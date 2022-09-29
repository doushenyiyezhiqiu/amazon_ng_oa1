from collections import Counter


def optimize_delivery(boxes):
    count = Counter(boxes)
    ans = 0
    for key in count:
        total = count[key]
        dp = [-1]*(total + 1)
        dp[0] = 0
        for num in [2, 3]:
            for i in range(num, total+1):
                dp[i] = dp[i-num]+1
        if dp[-1] == -1:
            return -1
        else:
            ans += dp[-1]
    return ans

print(optimize_delivery([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))


