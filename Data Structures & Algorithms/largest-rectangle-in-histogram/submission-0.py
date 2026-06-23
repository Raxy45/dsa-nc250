class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxA = -1
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1]>h:
                popped_idx, popped_height = stk.pop()
                maxA = max(maxA, (i - popped_idx)*popped_height)
                start = popped_idx
            stk.append((start, h))

        for i, h in stk:
            maxA = max(maxA, (len(heights) - i)*h)
        return maxA
        