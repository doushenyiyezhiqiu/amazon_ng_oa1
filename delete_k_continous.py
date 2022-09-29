def delete_k_continous_elements(arr, k):
    ans = sum(arr[k:])
    min_v = ans
    for i in range(k, len(arr)):
        min_v = min_v-arr[i]+arr[i-k]
        ans = min(ans, min_v)
    return ans

print(delete_k_continous_elements([7, 3, 6, 1], 2))