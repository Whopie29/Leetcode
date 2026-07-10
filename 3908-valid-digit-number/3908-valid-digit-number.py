class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        str_n=str(n)
        str_x=str(x)
        if str_x in str_n and not str_n.startswith(str_x):
            return True
        return False