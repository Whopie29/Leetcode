class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        res=[]
        for p,v in d.items():
            if v>k:
                v=k

            res+=[p]*v
           
        return res        
        