class Solution:
    def limitOccurrences(self, arr: list[int], k: int) -> list[int]:
        ''' d={}
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
           
        return res    '''    
        
        res = []
        cnt = 1

        res.append(arr[0])

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= k:
                res.append(arr[i])

        return res