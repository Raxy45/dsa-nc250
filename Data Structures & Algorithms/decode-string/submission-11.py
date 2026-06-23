class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            print(s[i], stk)
            if s[i] != ']':
                stk.append(s[i])
                continue
            
            char = ''
            while stk and stk[-1]!='[':
                char = stk.pop() + char
            stk.pop()

            num = ''
            while stk and stk[-1].isdigit():
                num = stk.pop() + num
            
            print(char)
            print(num)
            print(stk)
            chars = char * int(num)
            stk.append(chars)
        return "".join(stk)