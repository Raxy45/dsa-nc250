class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        def checkPali(l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1    
            return True

        def dfs(i):
            if i == len(s):
                ans.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if checkPali(i, j):
                    # lhs substring is pali
                    path.append(s[i:j+1])
                    dfs(j+1) # explore palis from next half -> can be > 1
                    path.pop()
        dfs(0)
        return ans
        