class Solution:
    def stoneGameII(self, piles):
        # Remember:
        # 1. Your turn:
        #     Maximize your score
        # 2. Opponent turn:
        #     Minimize their score

        # TC/SC:
            # 2 * (n+1) * (n+1) = n^2
        
        n = len(piles)
        dp = defaultdict(int)
        def solve(player, i, m):
            if i>=n: return 0

            if (player, i, m) in dp:
                return dp[(player, i, m)]
            result = float('-inf') if player==0 else float('inf')
            stones = 0
            for x in range(1,2*m+1):
                if (i+x)>n:
                    continue
                
                if player == 0:
                    # Alice
                    stones += piles[i+x-1]
                    result = max(result, stones+solve(1, i+x, max(m, x)))
                else:
                    # Bob
                    result = min(result, solve(0, i+x, max(m, x)))
            dp[(player, i, m)] = result
            return dp[(player, i, m)]
        return solve(0, 0, 1)
    def stoneGameIIMe(self, piles: List[int]) -> int:
        M, max_sum, n = 1, 0, len(piles)
        dp = defaultdict(int)
        def solve(i, m):
            if i==n:
                return 0
            
            if (i, m) in dp:
                return dp[(i, m)]
            max_sum = 0
            for j in range(1, (2*m + 1)):    
                if (i+j)<=n:
                    max_sum = max(sum(piles[i:]) - solve(i+j, max(m, j)), max_sum)
            dp[(i, m)] = max_sum
            return dp[(i, m)]
        return solve(0, 1)
            