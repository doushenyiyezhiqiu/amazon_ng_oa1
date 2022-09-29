def min_net_stock(stockPrice):
    min_month = 1
    n = len(stockPrice)
    left_sum = stockPrice[0]
    right_sum = sum(stockPrice[1:])
    min_v = abs(right_sum//(n-1)-left_sum)
    for i in range(1, n-1):
        left_sum += stockPrice[i]
        right_sum -= stockPrice[i]
        left = left_sum//(i+1)
        right = right_sum//(n-1-i)
        res = abs(left-right)
        if res == 0:
            return i+1
        elif res<min_v:
            min_v = res
            min_month = i+1
    return min_month

print(min_net_stock([1,3,2,4,5]))
