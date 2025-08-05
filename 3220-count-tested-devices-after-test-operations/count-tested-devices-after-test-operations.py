class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        c=0
        bat=batteryPercentages
        for i in range(len(bat)):
            if bat[i]>0:
                c+=1
                for j in range(i+1,len(bat)):
                    bat[j]=bat[j]-1
        return c
        