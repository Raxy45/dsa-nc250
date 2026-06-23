class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['[', '{', '(']:
                stk.append(c)
                continue
            if not stk: return False
            popped_c = stk.pop()
            if c == ']' and popped_c != '[': return False
            if c == '}' and popped_c != '{': return False
            if c == ')' and popped_c != '(': return False
        
        return len(stk) == 0