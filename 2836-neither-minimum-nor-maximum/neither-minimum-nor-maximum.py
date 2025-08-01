class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)==1:
            return -1
        m1=max(nums)
        m2=min(nums)
        nums.remove(m1)
        nums.remove(m2)
        if len(nums)==0:
            return -1
        return nums[0]
        