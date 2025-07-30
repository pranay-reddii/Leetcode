class Solution:
    def sortVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        l=[]
        for i in s:
            if i in vowels:
                l.append(ord(i))
        l.sort()
        lc=[]
        for i in l:
            lc.append(chr(i))
        
        f=[]
        start=0
        for i in s:
            if i not in vowels:
                f.append(i)
            else:
                f.append(lc[start])
                start+=1
        return "".join(f)

        

        