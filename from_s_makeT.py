def from_s_makeT(s, t):
    count_t = [0]*26
    count_s = [0]*26
    for ch in s:
        count_s[ord(ch)-ord('a')] += 1
    for ch in t:
        count_t[ord(ch)-ord('a')] += 1
    ans = float('inf')
    for i in range(26):
        if count_t[i] != 0 and count_s[i] != 0:
            ans = min(ans, count_s[i]//count_t[i])
        elif count_t[i] == 0 and count_s[i] != 0:
            return 0
    return ans

print(from_s_makeT('abacbc', 'abc'))