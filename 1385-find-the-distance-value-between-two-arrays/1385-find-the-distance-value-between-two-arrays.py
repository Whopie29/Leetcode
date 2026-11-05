class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        i=0
        cnt=0

        while i<len(arr1):
            j=0
            ok=True
            while j<len(arr2):
                if abs(arr1[i]-arr2[j]) <=d :
                    ok=False
                j+=1
            if ok:
                cnt+=1
            i+=1
        return cnt