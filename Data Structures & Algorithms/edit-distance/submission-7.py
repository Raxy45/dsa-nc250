class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1l, w2l = len(word1), len(word2)
        dp = [0] * (w2l+1)
        dp[w2l] = 1
        curr = 1
        nextDP = [0] * (w2l+1)
        for i in range(w2l+1):
            nextDP[i] = w2l-i
        for i in range(w1l-1, -1, -1):
            dp[w2l] = w1l-i
            for j in range(w2l-1, -1 ,-1):
                if word1[i] == word2[j]:
                    dp[j] = nextDP[j+1]
                    continue
                dp[j] = 1 + min(dp[j+1], # insert
                                   nextDP[j+1], # replace
                                   nextDP[j] # delete a char
                                   )
            nextDP = dp.copy()
        return nextDP[0]
class Solution2DDP:
    def minDistance(self, word1: str, word2: str) -> int:
        w1l, w2l = len(word1), len(word2)
        dp = [[0] *(w2l+1) for _ in range(w1l+1)]
        curr = w1l
        for i in range(w1l+1):
            dp[i][w2l] = curr
            curr -= 1
        
        curr = w2l
        for i in range(w2l+1):
            dp[w1l][i] = curr
            curr -= 1

        # or
            # base cases
        # for i in range(w1l + 1):
        #     dp[i][w2l] = w1l - i

        # for j in range(w2l + 1):
        #     dp[w1l][j] = w2l - j
        
        for i in range(w1l-1, -1, -1):
            for j in range(w2l-1, -1 ,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                    continue
                dp[i][j] = 1 + min(dp[i][j+1], # insert
                                   dp[i+1][j+1], # replace
                                   dp[i+1][j] # delete a char
                                   )
        return dp[0][0]
class SolutionRecMemo:
    def minDistance(self, word1: str, word2: str) -> int:
        w1l, w2l = len(word1), len(word2)
        dp = {}
        def solve(i, j):
            if j == w2l:
                return w1l-i
            
            if i==w1l:
                # meaning we have reached the end of w1, but w2 is still not formed
                return w2l - j # this denotes remaining number of chars which will be added to w1 to make up w2
            
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                print('word matched', i, j)
                dp[(i, j)] = solve(i+1, j+1)
                return dp[(i, j)]
                
            # This means word[i] != word2[j]
            # 3 options
            dp[(i, j)] = 1 + min(solve(i, j+1),   # insert
                       solve(i+1, j+1), # replace
                       solve(i+1, j)    # delete
                       )
            return dp[(i, j)]
        return solve(0, 0)