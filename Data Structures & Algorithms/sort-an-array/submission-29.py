class Solution:
    def sortArray(self, nums):
        def get_pivot(l, r):
            pivot_index = l
            pivot = nums[pivot_index]
            
            l += 1
            while l<=r:
                while l<=r and nums[l] <= pivot:
                    l += 1
                while r>=l and nums[r] >= pivot:
                    r -= 1
                
                if l<=r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            if nums[r] <= pivot:
                nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
                pivot_index = r
            return r
        def qs(l, r):
            if l<=r:
                pi = get_pivot(l, r)
                qs(l, pi-1)
                qs(pi+1, r)
        qs(0, len(nums)-1)
        # nums.reverse()
        return nums

    def sortArrayMS(self, nums: List[int]) -> List[int]:
        def mergeSort(l, mid, r):
            arr_1, arr_2 = nums[l:mid+1], nums[mid+1: r+1]
            idx = l
            i, j = 0, 0
            while i<len(arr_1) and j<len(arr_2):
                if arr_1[i] < arr_2[j]:
                    nums[l] = arr_1[i]
                    i += 1
                else:
                    nums[l] = arr_2[j]
                    j += 1
                l += 1
            
            while i<len(arr_1):
                nums[l] = arr_1[i]
                i += 1
                l += 1
            
            while j<len(arr_2):
                nums[l] = arr_2[j]
                j += 1
                l += 1

        def merge(l, r):
            if l<r:
                mid = (l+r)//2
                merge(l, mid)
                merge(mid+1, r)
                mergeSort(l, mid, r)
        merge(0, len(nums)-1)
        return nums