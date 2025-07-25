class Solution:
    def calPoints(self, operations: List[str]) -> int:
        num='0123456789'
        l=[]
        for i in operations:
            if i=="C":
                l.pop()
            elif i=="D":
                l.append(l[-1]*2)
            elif i=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        return sum(l)
            