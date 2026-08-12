class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp = Counter(t)
        n = len(s)
        smp = {}
        ans = s + t
        l, r = 0, 0
        curr_match = 0
        while r < len(s):
            if s[r] not in tmp:
                r += 1
                continue

            # s[r] in tmp:
            if s[r] not in smp:
                smp[s[r]] = 0
            smp[s[r]] += 1
            if smp[s[r]] == tmp[s[r]]:
                curr_match += 1
            while curr_match == len(tmp):
                # all freqs matched, start popping from lhs
                if len(s[l: r+1]) < len(ans):
                    ans = s[l:r+1]
                if s[l] not in tmp:
                    l += 1
                    continue
                smp[s[l]] -= 1
                if smp[s[l]] >= tmp[s[l]]:
                    l += 1
                    continue
                curr_match -= 1
                if smp[s[l]] == 0:
                    smp.pop(s[l])
                l += 1
            r += 1
        return ans if ans!=(s+t) else ""