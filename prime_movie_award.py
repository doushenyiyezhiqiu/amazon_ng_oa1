def prime_movie_award(awards, k):
    awards.sort()
    cur_min = awards[0]
    n = len(awards)
    ans = 1
    for i in range(1, n):
        if awards[i] > cur_min+k:
            ans += 1
            cur_min = awards[i]
    return ans

print(prime_movie_award([1,5,4,6,8,9,2], 3))
