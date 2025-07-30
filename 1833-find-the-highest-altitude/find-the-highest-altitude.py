class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[]
        l.append(0)
        ans=0
        for i in range(len(gain)):
            ans+=gain[i]
            l.append(ans)
        return max(l)
        