class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            elif i=="]":
                if not stack:
                    return False
                b=stack.pop()
                if b!="[":
                    return False
            elif i==")":
                if not stack:
                    return False
                b=stack.pop()
                if b!="(":
                    return False
            elif i=="}":
                if not stack:
                    return False
                b=stack.pop()
                if b!="{":
                    return False
        return not stack