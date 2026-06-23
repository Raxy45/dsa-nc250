class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = Counter(s1)
        s2_map = defaultdict(int)
        for i in range(len(s1)):
            char = s2[i]
            s2_map[char] = s2_map.get(char, 0) + 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True

            if (r-l+1) > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1
            s2_map[s2[r]] += 1
        return s1_map == s2_map