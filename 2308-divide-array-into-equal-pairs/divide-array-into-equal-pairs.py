class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        flag=True
        for i in range(0,len(nums),2):
            if nums[i]!=nums[i+1]:
                flag=False
        return flag

        