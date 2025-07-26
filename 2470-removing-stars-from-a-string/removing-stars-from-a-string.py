class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>=2 and i=="*":
                stack.pop()
                stack.pop()
        return "".join(stack)
        