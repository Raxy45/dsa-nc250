class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def get_pivot(l, r):
            pivot_index = l
            pivot = nums[pivot_index]
            
            l += 1
            while l<=r:
                while l<=r and nums[l] >= pivot:
                    l += 1
                while r>=l and nums[r] <= pivot:
                    r -= 1
                
                if l<=r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            if nums[r] >=pivot:
                nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
                pivot_index = r
            return pivot_index
                    
            
        l, r = 0, len(nums) - 1
        while l<=r:
            # print('l, r', l, r)
            pivot_index = get_pivot(l, r)
            # print('pivot_index is', pivot_index)
            if pivot_index == k - 1:
                return nums[pivot_index]
            
            # print('nums', nums)
            if pivot_index > k-1 : 
                r = pivot_index - 1
            else: 
                l = pivot_index + 1