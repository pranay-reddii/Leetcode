class Solution:
    def frequencySort(self, s: str) -> str:
        dici={}
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        ans=""
        for i in range(len(dici)):
            m=max(dici,key=dici.get)
            ans+=m*dici[m]
            del dici[m]
        return ans



        
        