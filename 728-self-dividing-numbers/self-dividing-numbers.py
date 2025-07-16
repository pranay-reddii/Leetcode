class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for num in range(left,right+1):
            num1=num
            li=[]
            flag=True
            while num>0:
                ki=num%10
                if ki==0:
                    flag=False
                    break
                li.append(ki)
                num=num//10
            for i in li:
                if num1%i!=0:
                    flag=False
                    break
            li=[]
            if flag:
                ans.append(num1)
        return ans






        
        