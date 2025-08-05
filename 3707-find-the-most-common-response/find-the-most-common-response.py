class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res=responses
        l=[]
        for i in res:
            l.append(list(set(i)))
    
        dici={}
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] not in dici:
                    dici[l[i][j]]=1
                else:
                    dici[l[i][j]]+=1
        m=max(dici.values())
        li=[key for key in dici if dici[key]==m]
        return min(li)
     






        