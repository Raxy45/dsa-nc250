class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] denotes whether s3[i+j:] can be formed by interleaving s1[i:] and s2[j:].
        # example can s1 = aaaa, s2=bbbb s3 = aabbbbaa then can suppose bbbbaa be formed from bbbb and aa
        # dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # dp[len(s1)][len(s2)] = True
        dp = [False] *(len(s2) + 1)
        dp[len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[j]:
                    dp[j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[j + 1]:
                    dp[j] = True
        print(dp)
        return dp[0]

    def isInterleave2D(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] denotes whether s3[i+j:] can be formed by interleaving s1[i:] and s2[j:].
        # example can s1 = aaaa, s2=bbbb s3 = aabbbbaa then can suppose bbbbaa be formed from bbbb and aa
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        print(dp)
        return dp[0][0]

    def isInterleaveTopDown(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        
        dp = {}
        def dfs(si, sj):
            if (si, sj) in dp:
                return dp[(si, sj)]
            # print(si, sj)
            if (si+sj) == len(s3):
                return True
            if si==len(s1) and sj==len(s2):
                return False
            
            if si<len(s1) and s1[si] == s3[si+sj]:
                if (dfs(si+1, sj)):
                    return True

            if sj<len(s2) and s2[sj] == s3[si+sj]:
                if dfs(si, sj+1):
                    return True
            dp[(si, sj)] = False
            return dp[(si, sj)]
        return dfs(0, 0)