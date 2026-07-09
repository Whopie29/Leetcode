class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[nums[0]]
        cnt=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                cnt+=1
            else:
                cnt=1
            
            if cnt<=k:
                res.append(nums[i])
        return res
