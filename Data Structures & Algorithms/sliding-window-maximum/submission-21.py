class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        ans, stk = [], deque()
        for j in range(len(nums)):
            # print('before', stk)
            while stk and nums[j] > nums[stk[-1]]:
                stk.pop()
            # print('mid', stk)
            stk.append(j)
            # since we're moving, how do we know if the left most ith char which should be removed
            # is present in stk or not?
            if j >=k-1:
                # print('adding to ans', j)
                ans.append(nums[stk[0]])
            # print('post stk', stk)
            # print('******')
        return ans















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

            # print(stk)
            if r>=k-1:
                ans.append(nums[stk[0]])
                # print(ans)
        return ans