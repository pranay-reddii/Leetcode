class Solution:
    def sortString(self, s: str) -> str:
        dici={}
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        dici1=sorted(dici)
        dici2=sorted(dici,reverse=True)
        ans=""
        while len(ans)<len(s):
            for i in dici1:
                if dici[i]>0:
                    ans+=i
                    dici[i]-=1
            for i in dici2:
                if dici[i]>0:
                    ans+=i
                    dici[i]-=1
        return ans
        
        
            
        
        