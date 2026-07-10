class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        digit_range=[]
        l=[]
        for i in nums:
            maxi=int(max(str(i)))
            mini=int(min(str(i)))
            l.append(maxi-mini)

        max_diff=max(l)
        sumi=0
        for i in range(len(l)):
            if l[i]==max_diff:
                sumi+=nums[i]
        return sumi
            


