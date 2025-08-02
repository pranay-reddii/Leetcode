class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dici={}
        for i in arr1:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
     
        res=[]
        for i in arr2:
            if i in arr1:
                res.extend([i]*dici[i])
        res1=[]
        for i in arr1:
            if i not in arr2:
                res1.append(i)
        res1.sort()
        return res+res1
        



        