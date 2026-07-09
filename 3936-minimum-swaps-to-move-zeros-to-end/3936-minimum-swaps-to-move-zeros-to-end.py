class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        nonZero = 0

        for num in nums:
            if num != 0:
                nonZero += 1

        swaps = 0
        for i in range(nonZero):
            if nums[i] == 0:
                swaps += 1

        return swaps

