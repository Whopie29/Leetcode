class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        arr = []

        for le in range(2, 10):
            for start in range(len(s) - le + 1):
                digit = int(s[start:start + le])

                if low <= digit <= high:
                    arr.append(digit)

        return sorted(arr)