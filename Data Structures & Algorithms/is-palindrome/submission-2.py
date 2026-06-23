class Solution:
    def isPalindrome(self, s: str) -> bool:
        # for i in range(0, len(s)-1):
        #     if s[i].isalnum():
        #         s[i] = s[i]

        s_p, e_p = 0, len(s)-1
        print(s)
        while s_p<=e_p:
            # print('s_p', s_p)
            # print('e_p', e_p)
            # print('*'*3)
            while s_p<len(s) and not s[s_p].isalnum():
                s_p += 1
            while e_p >= 0 and not s[e_p].isalnum():
                e_p -= 1
            

            if s_p<len(s) and e_p >= 0 and s[s_p].lower()!=s[e_p].lower():
                return False
            s_p += 1
            e_p -= 1
        return True
        