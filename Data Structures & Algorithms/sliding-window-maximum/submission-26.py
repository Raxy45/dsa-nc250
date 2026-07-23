class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stk = deque()
        i = 0
        ans = []
        for j in range(len(nums)):
            # print('b4', j, stk)
            while stk and nums[j] > nums[stk[0]]:
                stk.popleft()
            
            stk.append(j)
            if (j-k) >= stk[0]:
                stk.popleft()

            if j>=k-1:
                ans.append(nums[stk[0]])
            # print('after', j, stk)
        return ans