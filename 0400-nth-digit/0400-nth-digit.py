class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1
        
        # Step 1: Determine digit length
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
            
        # Step 2: Identify the number
        start += (n - 1) // length
        
        # Step 3: Extract the digit
        return int(str(start)[(n - 1) % length])