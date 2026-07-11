class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        num1=list(set(nums1))
        num2=list(set(nums2))
        l=[]
        for i in num1:
           
            if i not in num2:
                l.append(i)

            else:
                num2.remove(i)
        print(l)
        res.append(l)
        res.append(num2)
        return res
