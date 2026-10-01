class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(nums)):
            need=target-nums[i]

            if need in d:
                return [d[need],i]
        
            d[nums[i]]=i
            