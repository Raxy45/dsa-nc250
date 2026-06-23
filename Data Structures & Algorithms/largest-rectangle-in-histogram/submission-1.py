class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for index, height in enumerate(heights):
            while stk and height <= stk[-1][1]:
                popped_height_index, popped_height = stk.pop()
                curr_area = popped_height * (index-popped_height_index)
                max_area = max(max_area, curr_area)
                index = popped_height_index
            
            stk.append((index, height))
        
        for start_index, height in stk:
            max_area = max(max_area, (len(heights)-start_index)*height)
        return max_area