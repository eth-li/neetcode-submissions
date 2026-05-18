class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens:
            print(stack)
            if i == "+":
                new = stack[-1] + stack[-2]
                stack.pop()
                stack[-1] = new
            elif i == "*":
                new = stack[-1] * stack[-2]
                stack.pop()
                stack[-1] = new
            elif i == "/":
                new = stack[-2]/stack[-1]
                new = math.trunc(new)
                stack.pop()
                stack[-1] = new
            elif i == "-":
                new = stack[-2]-stack[-1]
                stack.pop()
                stack[-1] = new
            else:
                stack.append(int(i))
        return stack[0]