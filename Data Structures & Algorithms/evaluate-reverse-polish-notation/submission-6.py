class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in ops:
                ans = 0
                if token == "+":
                    ans = stack.pop() + stack.pop()
                elif token == "-":
                    ans = -1*(stack.pop() - stack.pop())
                elif token == "*":
                    ans = stack.pop() * stack.pop()
                else:
                    b = stack.pop()
                    a = stack.pop()
                    ans = int(a / b)
                stack.append(ans)
            else:
                stack.append(int(token))
        
        return stack[0]