class Solution:
    def get_Minimum_Cost(self, parcels, k):
        id = 1
        ans = 0
        while len(parcels) < k:
            if id in parcels:
                id += 1
                continue
            ans += id
            parcels.append(id)
            id += 1
        return ans

example1 = Solution()
parcels1 = [2, 3, 6, 10, 11]
k = 9
print(example1.get_Minimum_Cost(parcels1, k))
