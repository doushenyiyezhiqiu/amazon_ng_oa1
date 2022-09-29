def max_average_stock_price(nums, k):
    n = len(nums)
    ans = 0
    for i in range(n-k+1):
        if len(set(nums[i:i+k])) == k:
            ans = max(ans, sum(nums[i:i+k]))
    return ans

print(max_average_stock_price([1,2,7,7,4,3,6], 3))