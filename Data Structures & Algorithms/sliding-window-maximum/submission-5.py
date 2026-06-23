class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deck = deque()
        ans = []
        for i in range(0, len(nums)):
            while(len(deck)>0 and deck[0]<=(i-k)):
                deck.popleft()
             
            while(len(deck)>0 and nums[i]>=nums[deck[-1]]):
                deck.pop()
            
            deck.append(i)

            if i>=k-1:
                ans.append(nums[deck[0]])
        return ans
