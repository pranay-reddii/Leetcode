class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        ans1=0
        ans2=0
        for i in dici:
            ans1+=dici[i]//2
        for i in dici:
            if dici[i]%2==1:
                ans2+=1
        return [ans1,ans2]
