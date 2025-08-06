class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dici={}
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                return i
        