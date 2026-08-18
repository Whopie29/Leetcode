class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Only one window
        if k == n:
            return max(nums)

        freq = {}

        # Count occurrences in the entire array
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        ans = -1

        for i, x in enumerate(nums):
            # It must occur exactly once
            if freq[x] != 1:
                continue

            # Number of windows of length k containing index i
            left = max(0, i - k + 1)
            right = min(i, n - k)

            windows = right - left + 1

            if windows == 1:
                ans = max(ans, x)

        return ans