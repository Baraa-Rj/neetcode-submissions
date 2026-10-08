class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) ==1:
            return False
        stack = deque()
        chars = list(s)
        for c in s:
            if c == '(' or c =='{' or c == '[':
                stack.append(c)
            elif stack and c ==')' and stack[-1] != '(':
                return False
            elif stack and c =='}' and stack[-1] != '{':
                return False
            elif stack and c ==']' and stack[-1] != '[':
                return False
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack


            
        