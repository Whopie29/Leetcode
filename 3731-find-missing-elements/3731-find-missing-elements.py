class Solution:
    
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum=min(nums)
        maximum=max(nums)
    
        if maximum-minimum+1==len(nums):
            return []
        else:
            s=set(nums)
            res=[]
            for j in range(minimum,maximum+1):
                if j not in s:
                    res.append(j)

            return res

        