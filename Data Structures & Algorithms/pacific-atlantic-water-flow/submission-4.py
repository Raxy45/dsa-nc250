class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedGrid = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]
        
        # print(visitedGrid)
        # Pacific and Atlantic Marking
        # for r in range(len(heights)):
        #     for c in range(len(heights[r])):
        #         print(r, c)
        #         if (r==0 and c in range(len(heights[r]))) or (c==0 and r in range(len(heights))):
        #             visitedGrid[r][c][0] = True
                
        #         if (c==len(heights[r])-1 and r in range(len(heights))) or (r==len(heights)-1 and c in range(len(heights[r]))):
        #             visitedGrid[r][c][1] = True
                


        def dfs(r, c, prev_height, island_index):
            if min(r, c) < 0 or r==len(heights) or c == len(heights[0]):
                return
            
            if visitedGrid[r][c][island_index]:
                return
            
            # where to add the logic for comparing adjacent
            if heights[r][c] < prev_height:
                return

            visitedGrid[r][c][island_index] = True
            dfs(r, c+1, heights[r][c], island_index)
            dfs(r+1, c, heights[r][c], island_index)
            dfs(r, c-1, heights[r][c], island_index)
            dfs(r-1, c, heights[r][c], island_index)

        # for r in range(len(heights)):
        #     for c in range(len(heights[r])):
        #         if r==0 or c==0:
        #             # Traverse for Pacific
        #             dfs(r, c, float('-inf'), 0)
                
        #         if c==len(heights[r])-1 or r==len(heights)-1:
        #             dfs(r, c, float('-inf'), 1)
        for r in range(len(heights)):
            dfs(r, 0, float('-inf'), 0)
            dfs(r, len(heights[r])-1, float('-inf'), 1)

        for c in range(len(heights[0])):
            dfs(0, c, float('-inf'), 0)
            dfs(len(heights)-1, c, float('-inf'), 1)
        
        ans = []
        for r in range(len(visitedGrid)):
            for c in range(len(visitedGrid[r])):
                if visitedGrid[r][c][0] and visitedGrid[r][c][1]:
                    ans.append([r, c])
        return ans
            

        