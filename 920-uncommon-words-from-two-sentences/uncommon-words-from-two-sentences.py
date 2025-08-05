class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l=[]
        s=s1.split(" ")
        s3=s2.split(" ")
        fi=s+s3
        dici={}
        for i in fi:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for i in dici:
            if dici[i]==1:
                l.append(i)
        return l
        
        