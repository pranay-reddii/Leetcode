class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l=[]
        for i in range(len(A)):
            c=0
            for j in range(i+1):
                if B[j] in A[:i+1]:
                    c+=1
            l.append(c)
        return l
        