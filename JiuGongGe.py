import collections
def jiu_gong_ge(s):
    counter = collections.Counter(s)
    store = [[key, counter[key]] for key in counter]
    store.sort(key=lambda d:-d[1])
    print(store)
    length, i, m = len(store), 0, 0
    ans=['']*9
    used = [False]*26
    for j in range(9):
        if i<length:
            ans[j] += store[i][0]
            used[ord(store[i][0])-ord('a')]=True
            i += 1
        else:
            while used[m]:
                m += 1
            ans[j] += chr(ord('a')+m)
            m += 1

    for j in range(9):
        if i<length:
            ans[j] += store[i][0]
            used[ord(store[i][0])-ord('a')]=True
            i += 1
        else:
            while used[m]:
                m += 1
            ans[j] += chr(ord('a')+m)
            m += 1

    for j in range(8):
        if i<length:
            ans[j] += store[i][0]
            used[ord(store[i][0])-ord('a')]=True
            i += 1
        else:
            while used[m]:
                m += 1
            ans[j] += chr(ord('a')+m)
            m += 1
    return ans

print(jiu_gong_ge('abacadefghibj'))

