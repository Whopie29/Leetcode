class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        n = 1

        for i in range(1, min(a, b)+1):
            if a%i==b%i==0:
                n=i
        return n