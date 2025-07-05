class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l=[]
        res=float("inf")
        for i in range(len(nums)):
            ans=0
            while nums[i]>0:
                ans+=nums[i]%10
                nums[i]=nums[i]//10
            if i==ans:
                res=min(res,i)
        if res==float("inf"):
            return -1
        return res
                
        
            

        