class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=0
        for i in nums:
            if i<10:
                s+=i
        s1=sum(nums)-s
        if s==s1:
            return False
        return True

        