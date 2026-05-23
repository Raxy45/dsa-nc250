class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for indx, height in enumerate(heights):
            if stk and height > stk[-1][1]:
                # existing height in stk can be extended forward
                stk.append((indx, height))
                continue
            
            popped = False
            while stk and stk[-1][1] > height:
                popped = True
                popped_indx, popped_height = stk.pop()
                max_area = max(max_area, popped_height * (indx-popped_indx))
            if popped:
                indx = popped_indx
            stk.append((indx, height))
        print(stk)
        for indx, height in stk:
            print(indx, height)
            max_area = max(max_area, (len(heights) - indx) * height)
        return max_area





















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