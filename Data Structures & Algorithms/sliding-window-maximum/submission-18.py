class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, stk = [], deque()
        l = 0
        for r in range(len(nums)):
            # print(stk, l, r)
            if (r-l) == k:
                if l == stk[0]:
                    stk.popleft()
                l += 1
            
            while stk and nums[stk[-1]] <= nums[r]:
                stk.pop()
            stk.append(r)

            print(stk)
            if r>=k-1:
                # print('started adding ans for r and k', r, k)
                # print(stk[0], nums[stk[0]])
                ans.append(nums[stk[0]])
                # print(ans)
        return ans