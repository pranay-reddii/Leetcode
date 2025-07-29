class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        uniq=list(set(nums))
        for i in range(len(uniq)):
            for j in range(i+1,len(uniq)):
                a,b=uniq[i],uniq[j]
                if dici[a]>dici[b] or dici[a]==dici[b] and a<b:
                    uniq[i], uniq[j] = uniq[j], uniq[i]

        result = []
        for num in uniq:
            result.extend([num] * dici[num])
        
        return result