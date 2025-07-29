class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        for _ in range(len(nums)//2):
            l.append(nums.pop(1))
            l.append(nums.pop(0))
        return l

