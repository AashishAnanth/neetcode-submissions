class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for i in s:
            if i not in mappings:
                stack.append(i)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if mappings[i] != popped:
                    return False
        
        return not stack

