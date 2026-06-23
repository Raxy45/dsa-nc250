class Solution:
    def decodeString(self, s: str) -> str:
        def is_alpha(x):
            return ord('a') <= ord(x) and ord(x) <= ord('z') 
        final_ans = ""
        stk = []
        char_formed = ''
        num_formed = ''
        for c in s:
            # print(stk)
            if c != ']':
                # print('in first if')
                if c == '[':
                    # char formeed till now has to be num
                    print('adding ', num_formed, ' to stk')
                    stk.append(int(num_formed))
                    char_formed = ''
                    num_formed = ''
                    print(stk)
                elif c.isalpha():
                    # c is alpha
                    print('adding ', c, 'to char_formed ')
                    char_formed += c
                    print('char formed ', char_formed)
                elif c.isdigit():
                    num_formed += c
                    if len(char_formed) > 0:
                        stk.append(char_formed)
                        char_formed = ''
                # elif is_alpha_num(c):
                #     stk.append(c)
                # else:
                #     num_formed += c
            else:
                if len(char_formed) > 0:
                    stk.append(char_formed)
                char_to_repeat = ''
                print(stk)
                print('in main block')
                while len(stk) > 0 and not isinstance(stk[-1], int):
                    char_to_repeat = stk.pop() + char_to_repeat
                freq = stk.pop()
                curr_ans = char_to_repeat * int(freq)
                stk.append(curr_ans)
                char_formed = ''
        if len(char_formed) > 0:
            stk.append(char_formed)
        return "".join(stk)
                    
        