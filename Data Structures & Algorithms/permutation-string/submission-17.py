class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1mp, s2mp = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1mp[s1[i]] += 1
            s2mp[s2[i]] += 1
        if s1mp == s2mp: return True
        i = 0
        print(s1mp, s2mp)
        for j in range(len(s1), len(s2)):
            print(j-i+1, len(s1), i, j)
            if (j-i+1) > len(s1):
                s2mp[s2[i]] -= 1
                if s2mp[s2[i]] == 0: del s2mp[s2[i]]
                i += 1
            s2mp[s2[j]] += 1
            print(s1mp, s2mp)
            print(i, j)
            print('****')
            if s1mp == s2mp:
                return True
        return False



















        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        print(matches)
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26