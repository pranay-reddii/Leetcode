class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l=[]
        for i in range(1,target[-1]+1):
            l.append(i)
        li=[]
        for i in l:
            if i in target:
                li.append("Push")
            else:
                li.append("Push")
                li.append("Pop")
        return li

        