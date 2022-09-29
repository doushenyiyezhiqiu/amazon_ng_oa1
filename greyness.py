def greyness(array):
    m, n = len(array[0]), len(array)
    row_black = [0]*n
    column_black = [0]*m
    row_white = [0]*n
    column_white = [0]*m

    for i in range(n):
        row_black[i] = array[i].count('1')
        row_white[i] = m-1-row_black[i]

    for i in range(m):
        blacks, whites = 0, 0
        for j in range(n):
            if array[j][i] == '0':
                whites += 1
            else:
                blacks += 1
        column_black[i] = blacks
        column_white[i] = whites

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(abs((row_black[i]+column_black[j])-(row_white[i]+column_white[j])), ans)
    return ans

print(greyness([['1','1','0','1'],['0','1','0','1'],['1','0','1','0']]))

print(int('-2')<0)