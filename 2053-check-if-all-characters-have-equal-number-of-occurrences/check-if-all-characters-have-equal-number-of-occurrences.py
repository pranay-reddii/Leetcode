class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dici={}
        for i in s:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        flag=True
        l=list(set(s))
        for i in range(len(l)-1):
            if dici[l[i]]!=dici[l[i+1]]:
                flag=False
        return flag
        