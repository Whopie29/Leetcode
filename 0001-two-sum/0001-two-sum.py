class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            sumi = target - nums[i]
            
            if sumi in d:
                return d[sumi], i
            
            d[nums[i]] = i