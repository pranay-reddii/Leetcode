class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        if costs[0]>coins:
            return 0
        for i in range(len(costs)):
            ans+=costs[i]
            if ans>coins:
                return i
        return len(costs)
        

        