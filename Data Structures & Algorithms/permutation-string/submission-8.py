class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = Counter(s1)
        s2_map = {}
        for i in range(len(s1)):
            char = s2[i]
            s2_map[char] = s2_map.get(char, 0) + 1
        
        left, right = 0, len(s1)
        while right<len(s2):
            if s1_map == s2_map: return True

            if (right-left+1) > len(s1):
                char = s2[left]
                s2_map[char] -= 1
                if not s2_map[char]:
                    del s2_map[char]
                left += 1
            
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1
            right += 1
        return False