class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        digit_range=[]
        l=[]
        for i in nums:
            maxi=0
            mini=10000
            for j in str(i):
                maxi=max(maxi,int(j))
                mini=min(mini,int(j))
            diff=maxi-mini
            l.append(diff)
        
        max_diff=max(l)

        sumi=0
        for i in range(len(l)):
            if l[i]==max_diff:
                sumi+=nums[i]
        return sumi
            


