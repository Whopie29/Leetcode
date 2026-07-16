class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumi=0
        res=[]
        for i in range(len(nums)):
            
            sumi+=nums[i]
            res.append(sumi)
        return res