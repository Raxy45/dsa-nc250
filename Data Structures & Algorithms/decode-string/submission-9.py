class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        ans = ""
        for char in s:
            print(stk)
            if char!=']':
                stk.append(char)
                continue
            
            rep_str = ""
            while stk and not stk[-1].isdigit():
                if stk[-1] == '[': 
                    stk.pop()
                    continue
                rep_str = stk.pop() + rep_str
            
            multiplier = int(stk.pop())
            string_to_push = rep_str * multiplier
            print(string_to_push)
            stk.append(string_to_push)
        print(stk)
        return "".join(stk)