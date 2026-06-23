class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = [0]*26
        s2_dict = [0]*26

        for i in range(len(s1)):
            s1_dict[ord(s1[i]) - ord('a')] += 1
            s2_dict[ord(s2[i]) - ord('a')] += 1
        
        if len(s2)<len(s1):
            return False
        
        # print(s1)
        # print(s1_dict)

        l = 0
        r = len(s1)
        
        while r<=len(s2):
            print(l, r)
            print('current substring: ', s2[l:r])
            print('current dict: ', s2_dict)
            if s2_dict == s1_dict:
                return True
            print('removing s2[l]: ', s2[l])
            s2_dict[ord(s2[l])-ord('a')] -= 1
            print('post removal: ')
            print(s2_dict)
            print('after removing l,r', l, r)
            l += 1
            if r<len(s2):
                s2_dict[ord(s2[r])-ord('a')] += 1
            r += 1
        return False