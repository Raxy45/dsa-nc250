class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deq = deque()
        l = 0
        for r in range(len(nums)):
            if deq and r-k >= deq[0]:
                deq.popleft()

            while deq and nums[r]>=nums[deq[-1]]:
                deq.pop()
            
            deq.append(r)
            if r>=k-1:
                ans.append(nums[deq[0]])
        
        return ans