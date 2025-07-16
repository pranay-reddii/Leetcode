class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for num in range(low,high+1):
            num=str(num)
            n=len(num)
            if n % 2 != 0:
                continue
            num1=num[:n//2]
            num2=num[n//2:]
            num1=int(num1)
            num2=int(num2)
            ans1=0
            ans2=0
            while num1>0:
                ans1+=num1%10
                num1=num1//10
            while num2>0:
                ans2+=num2%10
                num2=num2//10
            if ans1==ans2:
                c+=1
        return c






        