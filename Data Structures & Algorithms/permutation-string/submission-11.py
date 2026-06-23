class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        match = 26
        hmp1, hmp2 = [0]*26, [0]*26

        def g_o(char):
            return ord(char) - ord('a')
            
        for i in range(len(s1)):
            hmp1[g_o(s1[i])] += 1
            hmp2[g_o(s2[i])] += 1
            if hmp1[g_o(s2[i])] != hmp2[g_o(s2[i])]:
                match -= 1

        print(hmp1)
        print('initial match count', match)
        for i in range(len(s1), len(s2)):
            char = s2[i]
            hmp2[g_o(char)] += 1
            print('current char', char)
            print(f'{hmp1 = }')
            print(f'{hmp2 = }')
            if hmp2[g_o(char)] == hmp1[g_o(char)]:
                match += 1
            
            if hmp2[g_o(char)]-1 == hmp1[g_o(char)]: 
                match -= 1
            
            if hmp2[g_o(char)] + 1 == hmp1[g_o(char)]:
                match -= 1

            print('updated match', match)
            print('*'*6)
            if match == 26:
                return True
        
        return False
        
        