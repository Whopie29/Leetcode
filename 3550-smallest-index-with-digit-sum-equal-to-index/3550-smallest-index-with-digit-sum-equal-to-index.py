class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumi(n):
            s=0
            for i in str(n):
                s+=int(i)
            return s
            
        for i,j in enumerate(nums):
            if i==sumi(j):
                return i
        return -1