class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        start=0
        for i in range(len(nums)):
            if nums[i]-nums[start]>k:
                count+=1
                start=i
        return count+1

        