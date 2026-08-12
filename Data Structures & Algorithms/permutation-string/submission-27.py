class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        tmp = Counter(s1)
        smp = {}
        curr_match = 0
        for i in range(len(s1)):
            if s2[i] in tmp:
                if s2[i] not in smp:
                    smp[s2[i]] = 0
                smp[s2[i]] += 1
                if smp[s2[i]] == tmp[s2[i]]:
                    curr_match += 1
        if curr_match == len(tmp):
            return True
        l = 0
        # print(smp, tmp, curr_match)
        for r in range(len(s1), len(s2)):
            if s2[r] in tmp:
                if s2[r] not in smp:
                    smp[s2[r]] = 0
                smp[s2[r]] += 1
                if smp[s2[r]] == tmp[s2[r]]:
                    curr_match += 1
            
            if s2[l] in tmp:
                smp[s2[l]] -= 1
                if smp[s2[l]] == tmp[s2[l]]:
                    curr_match -= 1
                if smp[s2[l]] == 0:
                    smp.pop(s2[l])
            l += 1
            if curr_match == len(tmp):
                return True
        if curr_match == len(tmp):
            return True
        return False
            
        