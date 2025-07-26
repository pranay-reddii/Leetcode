class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>=2 and abs(ord(stack[-1])-ord(stack[-2]))==32:
                stack.pop()
                stack.pop()
        return "".join(stack)
        