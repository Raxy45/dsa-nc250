class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        cmp, tmp, diff = [0]*26, [0]*26, 26
        for i in range(len(s1)):
            cmp[ord(s1[i]) - ord('a')] += 1
            tmp[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            if cmp[i] == tmp[i]:
                diff -= 1
        print(diff)
        print(cmp)
        print(tmp)
        if diff == 0:
            return True
        
        i = 0
        for j in range(len(s1), len(s2)):
            # First removing one char from LHS, as we are adding one new after this
            tmp[ord(s2[i]) - ord('a')] -= 1
            if (tmp[ord(s2[i]) - ord('a')] + 1) == cmp[ord(s2[i]) - ord('a')]:
                print('we removed a char, which was previously matching')
                print(s2[i])
                diff += 1
            elif tmp[ord(s2[i]) - ord('a')] == cmp[ord(s2[i]) - ord('a')]:
                # we removed a char which was not present in s1, therefore diff reduced by one
                diff -= 1
            i += 1

            # adding char
            tmp[ord(s2[j]) - ord('a')] += 1
            if (tmp[ord(s2[j]) - ord('a')] - 1) == cmp[ord(s2[j]) - ord('a')]:
                print('Earlier it was matching but now we added 1 and made it unmatch', s2[j])
                diff += 1

            if tmp[ord(s2[j]) - ord('a')] == cmp[ord(s2[j]) - ord('a')]:
                diff -= 1
            print(diff)
            print('*****')
            if diff == 0:
                return True
        return False
        

    def checkInclusionMeHashMap(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1mp, s2mp = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1mp[s1[i]] += 1
            s2mp[s2[i]] += 1
        if s1mp == s2mp: return True
        i = 0
        # print(s1mp, s2mp)
        for j in range(len(s1), len(s2)):
            # print(j-i+1, len(s1), i, j)
            if (j-i+1) > len(s1):
                s2mp[s2[i]] -= 1
                if s2mp[s2[i]] == 0: del s2mp[s2[i]]
                i += 1
            s2mp[s2[j]] += 1
            # print(s1mp, s2mp)
            # print(i, j)
            # print('****')
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