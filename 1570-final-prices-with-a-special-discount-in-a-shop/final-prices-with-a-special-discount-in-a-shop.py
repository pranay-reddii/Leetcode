class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l=[]
        for i in range(len(prices)):
            dis=False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    l.append(prices[i]-prices[j])
                    dis=True
                    break
            if not dis:
                l.append(prices[i])
        return l

        