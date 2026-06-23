class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        slow = 0
        ans = []
        for fast in range(len(nums)):
            print(q, slow, fast)
            if q and fast-slow == k:
                # we have hit max window limit
                if slow == q[-1]:
                    q.popleft()
                slow += 1
            
            while q and nums[fast] >= nums[q[0]]:
                q.popleft()
            
            q.append(fast)
            if fast-slow==k-1:
                ans.append(nums[q[0]])
            print(ans)
            print('*'*4)
        return ans