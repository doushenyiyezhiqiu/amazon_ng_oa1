# only consider 101 and 010 these two situations, when search element in book iteratively
# , if book[i] equals 1, make answer plus total left zeroes mutiple total right zeroes, etc
# Time complexity: O(n)
# Space complexity: O(n)

def how_to_count(book):
    n = len(book)
    left_zero = [0] * n
    left_one = [0] * n
    right_zero = [0] * n
    right_one = [0] * n
    ans = 0
    for i in range(n-2, 0, -1):
        if book[i+1] == '0':
            right_zero[i] = right_zero[i+1] + 1
            right_one[i] = right_one[i+1]
        else:
            right_zero[i] = right_zero[i+1]
            right_one[i] = right_one[i+1] + 1
    for i in range(1, n - 1):
        if book[i - 1] == '0':
            left_zero[i] = left_zero[i - 1] + 1
            left_one[i] = left_one[i - 1]
        else:
            left_zero[i] = left_zero[i - 1]
            left_one[i] = left_one[i - 1] + 1
        if book[i] == '1':
            ans += left_zero[i] * right_zero[i]
        else:
            ans += left_one[i] * right_one[i]
    return ans

print(how_to_count('01001'))