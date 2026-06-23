class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # App 1:
        # 1. Traverse each cell
        # 2. For each cell check if its water can flow to both Atlantic and Pacific

        # App 2:
        # 1. Traverse from ends
        # 2. Water will go to neighbouring cell if height neighboring>

        R, C = len(heights), len(heights[0])
        h_mp = [[[False, False] for _ in range(C)] for _ in range(R)]
        
        def solve(r, c, prev_h, idx):
            if min(r, c) < 0 or r==R or c==C or h_mp[r][c][idx] or heights[r][c]<=prev_h:
                # print('return: height', r,c, 'less then', prev_h)
                return
            
            # print('height',r,c, 'gt than', prev_h)
            h_mp[r][c][idx] = True
            solve(r, c+1, heights[r][c], idx)
            solve(r+1, c, heights[r][c], idx)
            solve(r, c-1, heights[r][c], idx)
            solve(r-1, c, heights[r][c], idx)

        for r in range(R):
            for c in range(C):
                if r==0 or c==0:
                    # print('solving for Pacific for',r,c)
                    solve(r,c, float('-inf'), 0)
                
                if r==R-1 or c==C-1:
                    # print('solving for Atlantic for', r,c)
                    solve(r, c, float('-inf'), 1)
        
        print(h_mp)
        ans = []
        for r in range(R):
            for c in range(C):
                if h_mp[r][c][0] and h_mp[r][c][1]:
                    ans.append([r, c])
        return ans
        