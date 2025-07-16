class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            num=str(num)
            if len(num)%2==0:
                ans+=1
        return ans

        