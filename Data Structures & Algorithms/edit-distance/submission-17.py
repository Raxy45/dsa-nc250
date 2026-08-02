class Solution:
    def minDistance(self, w1, w2):
        dp = [[0] * (len(w2) + 1) for _ in range((len(w1)+1))]
        w1l = len(w1)
        for i in range(len(w1)):
            dp[i][len(w2)] = w1l
            w1l -= 1
        
        for i in range(len(w2)):
            dp[len(w1)][i] = len(w2)-i
        # print(dp)
        
        for r in range(len(w1)-1, -1, -1):
            for l in range(len(w2)-1, -1, -1):
                if w1[r] == w2[l]:
                    dp[r][l] = dp[r+1][l+1]
                    continue
                dp[r][l] = 1 + min(dp[r+1][l+1], dp[r][l+1], dp[r+1][l])
        return dp[0][0]

                
    def minDistance2(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(l, r):
            if (l, r) in dp: return dp[(l, r)]
            if l==len(word1) and r==len(word2): return 0
            if l==len(word1):
                return len(word2) - r
            if r==len(word2):
                return len(word1) - l
            
            curr = float('inf')
            if word1[l] == word2[r]:
                curr = dfs(l+1, r+1)
            else:
                curr = 1 + min(dfs(l+1, r), #delete 
                               dfs(l+1, r+1), # replace
                               dfs(l, r+1) # insert
                               )
            dp[(l, r)] = curr
            return dp[(l, r)]
        return dfs(0, 0)
            
        