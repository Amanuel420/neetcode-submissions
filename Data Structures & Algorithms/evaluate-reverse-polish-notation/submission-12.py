class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]

        for i in tokens:
            if i=="+":
                val1,val2=s.pop(),s.pop()
                val=val2+val1
                s.append(val)

            elif i=="-":
                val1,val2=s.pop(),s.pop()
                val=val2-val1
                s.append(val)

            elif i=="*":
                val1,val2=s.pop(),s.pop()
                val=val2*val1
                s.append(val)

            elif i=="/":
                val1,val2=s.pop(),s.pop()
                val=int(val2/val1)
                s.append(val)

            else: 
                v=int(i)
                s.append(v)

        return int(s[0])