class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        A=int(a,2)
        B=int(b,2)
        s=A+B
        return str(bin(s)).replace("0b","")
        