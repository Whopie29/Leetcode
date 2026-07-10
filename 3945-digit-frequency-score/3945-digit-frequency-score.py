class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        l=[]
        for i in str(n):
            l.append(int(i))

        d={}
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            
        sumi=0
        for k,v in d.items():
            sumi+=(k*v)
        return sumi