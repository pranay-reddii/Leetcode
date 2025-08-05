class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        dici={}
        for i in arr:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for i in dici:
            if i==dici[i]:
                l.append(i)
        if len(l)>=1:
            return max(l)
        return -1

        