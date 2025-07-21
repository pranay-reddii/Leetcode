class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=[]
        for i in range(len(names)):
            people.append((heights[i],names[i]))
        people.sort(reverse=True)
        l=[]
        for height,name in people:
            l.append(name)
        return l

        