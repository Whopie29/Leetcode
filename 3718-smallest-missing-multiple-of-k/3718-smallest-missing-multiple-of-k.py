class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen=set(nums)
        l=[]
        for i in range(1,1000):
            if i not in seen and i%k==0:
                l.append(i)
        if l:

            return l[0]
        