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
            while stk and stk[-1].isalpha():
                rep_str = stk.pop() + rep_str
            
            print('xxx')
            print(rep_str)
            print(stk)
            print('xxx')
            stk.pop()
            multiplier = ""
            while stk and stk[-1].isdigit():
                multiplier = stk.pop() + multiplier
            print(multiplier)
            multiplier = int(multiplier)
            string_to_push = rep_str * multiplier
            print(string_to_push)
            stk.append(string_to_push)
        print(stk)
        return "".join(stk)