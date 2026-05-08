class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "{" or i =="[" or i=="(":
                stack.append(i)
            elif not stack:
                return False
            elif (i=="}" and not stack[-1] == "{") or (i=="]" and not stack[-1] == "[") or (i==")" and not stack[-1] == "("):
                return False
            else:
                stack.pop()
        return not stack