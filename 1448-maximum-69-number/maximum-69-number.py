class Solution:
    def maximum69Number (self, num: int) -> int:
        ar=list(str(num))
        for i in range(len(ar)):
            if ar[i]!="9":
                ar[i]="9"
                break
        return int("".join(ar))




        