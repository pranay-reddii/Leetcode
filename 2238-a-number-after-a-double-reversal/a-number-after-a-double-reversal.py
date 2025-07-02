class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(num):
            if num==0:
                return 0
            ans=""
            while num>0:
                ans+=str(num%10)
                num=num//10
            return int(ans)
            
        ans1=reverse(num)
        ans2=reverse(ans1)
        return ans2==num
