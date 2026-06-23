class Solution:
    def decodeString(self, s: str) -> str:
        final_ans = ""
        stk = []
        char_formed = ''
        num_formed = ''
        for c in s:
            if c != ']':
                if c == '[':
                    stk.append(int(num_formed))
                    char_formed = ''
                    num_formed = ''
                elif c.isalpha():
                    char_formed += c
                elif c.isdigit():
                    num_formed += c
                    if len(char_formed) > 0:
                        stk.append(char_formed)
                        char_formed = ''
            else:
                char_to_repeat = ''
                while len(stk) > 0 and not isinstance(stk[-1], int):
                    char_to_repeat = stk.pop() + char_to_repeat
                freq = stk.pop()
                curr_ans = char_to_repeat * int(freq)
                stk.append(curr_ans)
                char_formed = ''
        if len(char_formed) > 0:
            stk.append(char_formed)
        return "".join(stk)
                    
        