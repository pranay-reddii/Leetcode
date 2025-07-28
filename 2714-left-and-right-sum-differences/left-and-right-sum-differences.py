class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            left=0
            right=0
            for j in range(0,i):
                left+=nums[j]
            for j in range(i+1,len(nums)):
                right+=nums[j]
            l.append(abs(left-right))
        return l

