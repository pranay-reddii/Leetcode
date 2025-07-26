class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        for i in s:
            stack.append(i)
            n=len(part)
            if len(stack)>=n and "".join(stack[-n:])==part:
                for i in range(n):
                    stack.pop()
              
        return "".join(stack)

        