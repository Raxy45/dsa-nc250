class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for index, height in enumerate(heights):
            print(height, index)
            while stk and height <= stk[-1][1]:
                popped_height_index, popped_height = stk.pop()
                curr_area = popped_height * (index-popped_height_index)
                print('popped', index)
                print(popped_height_index, popped_height, curr_area)
                max_area = max(max_area, curr_area)
                if stk and height > stk[-1][1]:
                    index = popped_height_index
            
            stk.append((index, height))
            print(stk, max_area)
            print('*'*4)
        for start_index, height in stk:
            print(max_area, (len(heights)-start_index)*height)
            max_area = max(max_area, (len(heights)-start_index)*height)
        return max_area