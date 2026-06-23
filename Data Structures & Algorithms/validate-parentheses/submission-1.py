class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in s:
            print('i ', i)
            print('stl', stack)
            if i == ')':
                prev_brack = stack[-1]
                if prev_brack != '(':
                    return False
                stack.pop()
            elif i == ']':
                prev_brack = stack[-1]
                if prev_brack != '[':
                    return False
                stack.pop()
            elif i == '}':
                prev_brack = stack[-1]
                if prev_brack != '{':
                    return False
                stack.pop()
            else:
                stack.append(i)
        return True