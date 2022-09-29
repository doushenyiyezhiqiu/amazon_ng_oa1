def common_prefix(inputs):
    n = len(inputs)
    ans = [0]*n
    for i in range(n):
        suffix = inputs[i:]
        begin = 0
        while begin < len(suffix):
            if suffix[begin] != inputs[begin]:
                break
            begin += 1
        ans[i] = begin

    return ans

print(common_prefix('abcabcd'))