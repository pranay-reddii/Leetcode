class Solution:
    def maxFreqSum(self, s: str) -> int:
        v='aeiou'
        c=''
        v1=''
        for i in s:
            if i in v:
                v1+=i
            else:
                c+=i
        dici1={}
        dici2={}
        for i in v1:
            if i not in dici1:
                dici1[i]=1
            else:
                dici1[i]+=1
        for i in c:
            if i not in dici2:
                dici2[i]=1
            else:
                dici2[i]+=1
        ans1=max(dici1.values(),default=0)
        ans2=max(dici2.values(),default=0)
        return ans1+ans2

        