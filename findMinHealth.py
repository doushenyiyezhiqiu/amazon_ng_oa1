class Solution:
    def calPlayerMinHealth(self,power,armor):
        return sum(power)-min(max(power),armor)+1

power1=[1,2,6,7]
armor1=5
solution1=Solution()
print(solution1.calPlayerMinHealth(power1,armor1))