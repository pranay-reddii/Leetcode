class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        num='0123456789'
        for i in s:
            if i not in num:
                stack.append(i)
            if i in num:
                stack.pop()
        return "".join(stack)

        