class Solution:
    def merge(self, arr, l, m, r):
        left_a, right_a = arr[l:m+1], arr[m+1:r+1]
        left_index = right_index = 0
        sorted_index = l

        while left_index < len(left_a) and right_index < len(right_a):
            if left_a[left_index] < right_a[right_index]:
                arr[sorted_index] = left_a[left_index]
                left_index += 1
            else:
                arr[sorted_index] = right_a[right_index]
                right_index += 1
            sorted_index += 1
        
        while left_index < len(left_a):
            arr[sorted_index] = left_a[left_index]
            left_index += 1
            sorted_index += 1
        
        while right_index < len(right_a):
            arr[sorted_index] = right_a[right_index]
            right_index += 1
            sorted_index += 1
            

    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, l, r):
            if l == r:
                return
            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)
            return arr
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums
        