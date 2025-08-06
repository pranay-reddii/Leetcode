class Solution:
    def minimumLength(self, s: str) -> int:
        dici={}
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for i in dici:
            
            while dici[i]>2:
                dici[i]-=2
        return sum(dici.values())
        