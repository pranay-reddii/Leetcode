class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l=[]
        
        for num in nums:
            ans=""
            while num>0:
                ans+=str(num%10)
                num=num//10
            l.append(int(ans))
        res=nums+l
        return len(set(res))



            

        