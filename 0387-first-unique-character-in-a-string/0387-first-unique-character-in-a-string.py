class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        l=[]
        for k,v in d.items():
            if v==1:
                l.append(k)

        if l:
            return s.index(l[0])
        return -1