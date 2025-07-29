class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
    
        n=len(piles)//3
        ans=0
        for i in range(n):
            ans+=piles[i*2+1]
        return ans

        