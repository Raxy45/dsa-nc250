class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        islands = {
            'P': set(),
            'A': set()
        }
        def traverse(r, c, island, prev_height):
            if min(r, c)<0 or r==len(heights) or c==len(heights[0]) \
            or (r, c) in islands[island] or heights[r][c]<=prev_height: return
            islands[island].add((r, c))

            traverse(r, c+1, island, heights[r][c])
            traverse(r, c-1, island, heights[r][c])
            traverse(r+1, c, island, heights[r][c])
            traverse(r-1, c, island, heights[r][c])
        

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0 and (i, j) not in islands['P']:
                    # Pacific
                    traverse(i, j, 'P', float('-inf'))

                if i==len(heights)-1 or j==len(heights[0])-1 \
                and (i, j) not in islands['A']:
                    # atlantic
                    traverse(i, j, 'A', float('-inf'))
        
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in islands['P'] and (i, j) in islands['A']:
                    ans.append((i, j))
        return ans