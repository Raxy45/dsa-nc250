class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for i, height in enumerate(heights):
            start_idx = i
            while stk and height < stk[-1][0]:
                popped_height, popped_height_idx = stk.pop()
                curr_area = popped_height * (i-popped_height_idx)
                max_area = max(max_area, curr_area)
                start_idx = popped_height_idx
            stk.append((height, start_idx))

        for height, start_idx in stk[::-1]:
            max_area = max(max_area, height*(len(heights)-start_idx))
        return max_area








        stk = []
        max_area = 0
        for index, height in enumerate(heights):
            print(height, index)
            curr_start_index = index
            while stk and height < stk[-1][1]:
                popped_height_index, popped_height = stk.pop()
                curr_area = popped_height * (index-popped_height_index)
                print('popped', index)
                print(popped_height_index, popped_height, curr_area)
                max_area = max(max_area, curr_area)
                curr_start_index = popped_height_index
            
            stk.append((curr_start_index, height))
            print(stk, max_area)
            print('*'*4)
        for start_index, height in stk:
            print(max_area, (len(heights)-start_index)*height)
            max_area = max(max_area, (len(heights)-start_index)*height)
        return max_area