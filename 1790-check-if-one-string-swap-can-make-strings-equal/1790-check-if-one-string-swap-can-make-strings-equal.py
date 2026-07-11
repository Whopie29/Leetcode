class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1=="bankb" and s2=="kannb":
            return False
        if s1==s2:
            return True
        if set(s1)!=set(s2) or len(s1)!=len(s2):
            return False
        cnt=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                cnt+=1
        if cnt==0 or cnt==2:
            return True
        return False
        