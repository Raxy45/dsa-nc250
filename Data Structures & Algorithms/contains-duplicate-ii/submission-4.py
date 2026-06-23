class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        R = 0
        window = set()
        for r in range(len(nums)):
            # print('nums[l], nums[r] ', nums[L], nums[r])
            # print('window ', window)
            if r-L>k:
                window.remove(nums[L])
                L += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        
        return False

        while R<len(nums):
            if len(window)+1 > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            window.add(nums[R])
            R += 1
        window = set()
        L = R = 0
        while R < len(nums):
            if R-L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
            R += 1
        return False