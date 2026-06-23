class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, part = [], []

        def solve(idx):
            if idx == len(s):
                ans.append(part.copy())
                return

            for j in range(idx, len(s)):
                if self.isValidPali(s, idx, j):
                    part.append(s[idx:j+1])
                    solve(j+1)
                    part.pop()
            
        solve(0)
        return ans

    def isValidPali(self, s, i, j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
        return True