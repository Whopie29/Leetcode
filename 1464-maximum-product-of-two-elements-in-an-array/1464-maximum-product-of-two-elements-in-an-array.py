class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''maxi=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pro=(nums[i]-1)*(nums[j]-1)
                maxi=max(maxi,pro)
        return maxi'''
        nums.sort()
        return (nums[-2]-1) * (nums[-1]-1)