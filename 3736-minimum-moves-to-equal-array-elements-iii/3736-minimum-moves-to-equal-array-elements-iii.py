class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        sumi=0
        for i in nums:
            sumi+=maxi-i
        return sumi