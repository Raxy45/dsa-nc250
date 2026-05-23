class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        i, j = 0, 1
        w.add(nums[i])
        while j<len(nums):
            # print(w)
            while (j-i) <= k:
                # print('inside of inner while')
                # print(nums[j], w, i, j)
                if nums[j] in w:
                    return True
                w.add(nums[j])
                j += 1
            w.remove(nums[i])
            i += 1
        return False















        i = 0
        window = set()
        for j in range(len(nums)):
            if (j-i)>k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window: return True
            window.add(nums[j])
        return False