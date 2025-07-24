class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dici1={}
        for i in s:
            if i not in dici1:
                dici1[i]=1
            else:
                dici1[i]+=1
        dici2={}
        for i in t:
            if i not in dici2:
                dici2[i]=1
            else:
                dici2[i]+=1
        ans=0
        for i in dici1:
            if i not in dici2:
                ans+=dici1[i]
            elif dici1[i]>dici2[i]:
                ans+=dici1[i]-dici2[i]
        return ans


        