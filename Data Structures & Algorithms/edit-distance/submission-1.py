class Solution:
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