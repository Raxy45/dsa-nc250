class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        temp_set = set()
        for j in range(len(nums)):
            if j-i>k:
                set.remove(nums[i])
                i+=1
            
            if nums[j] in temp_set:
                return True
            temp_set.add(nums[j])
        return False


        L = 0
        R = 0
        window = set()
        for r in range(len(nums)):
            if r-L>k:
                window.remove(nums[L])
                L += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        
        return False