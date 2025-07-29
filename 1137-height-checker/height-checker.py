class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        h1=sorted(heights)
        c=0
        for i in range(n):
            if heights[i]!=h1[i]:
                c+=1
        return c



        