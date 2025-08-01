class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        dici={}
        for i in target:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        dici1={}
        for i in arr:
            if i not in dici1:
                dici1[i]=1
            else:
                dici1[i]+=1
        flag=False
        for i in target:
            if i in arr:
                if dici[i]==dici1[i]:
                    flag=True
                else:
                    return False
            else:
                return False
        return flag