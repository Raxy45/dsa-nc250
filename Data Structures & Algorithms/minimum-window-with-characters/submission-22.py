class Solution:
    def minWindow(self, s: str, t: str) -> str:
        imp, tmp = defaultdict(int), {}
        tmp = Counter(t)
        print(tmp)

        required = len(tmp)
        ans = len(s)+1
        ans_str = ""
        j = 0
        for i in range(len(s)):
            imp[s[i]] += 1
            if imp[s[i]] == tmp[s[i]]:
                required -= 1
            
            while required == 0 and j<=i:
                # print(imp, tmp, j, i)
                if (i-j+1) < ans:
                    ans = (i-j+1)
                    ans_str = s[j:i+1]
                imp[s[j]] -= 1
                if imp[s[j]] < tmp[s[j]]:
                    required += 1
                j += 1
        return ans_str