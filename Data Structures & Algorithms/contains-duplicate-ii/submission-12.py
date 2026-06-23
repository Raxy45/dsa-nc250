class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        if len(nums) == 1: return False
        for i in range(k+1):
            if nums[i] in window: return True
            window.add(nums[i])
        
        print(window)
        l = 0
        for r in range(k+1, len(nums)):
            # print(window)
            # print(nums[r])
            if len(window) >= k+1:
                window.remove(nums[l])
                l += 1
            
            if nums[r] in window: return True
            window.add(nums[r])
        return False