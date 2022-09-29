def router(building_count, router_location, router_range):
    n = len(building_count)
    add = [0]*(n+1)
    for i in range(len(router_location)):
        add[max(0, router_location[i]-router_range[i]-1)] += 1
        add[min(n, router_location[i]+router_range[i])] -= 1
    count,ans = 0, 0
    for i in range(n):
        count += add[i]
        if count >= building_count[i]:
            ans += 1
    return ans

print(router([1, 4, 2, 3, 2], [3, 1], [2, 3]))
