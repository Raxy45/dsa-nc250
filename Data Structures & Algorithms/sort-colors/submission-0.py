class Solution:
    def merge(self, arr, L, M, H):
        left_a = arr[L:M+1]
        right_a = arr[M+1:H+1]

        current_index = L
        left_i, right_i = 0, 0

        while left_i < len(left_a) and right_i < len(right_a):
            if left_a[left_i] <= right_a[right_i]:
                arr[current_index] = left_a[left_i]
                left_i += 1
            else:
                arr[current_index] = right_a[right_i]
                right_i += 1
            current_index += 1

        while left_i < len(left_a):
            arr[current_index] = left_a[left_i]
            left_i += 1
            current_index += 1
        while right_i < len(right_a):
            arr[current_index] = right_a[right_i]
            right_i += 1
            current_index += 1
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(arr, low, high):
            if low == high:
                return
            mid = (low+high)//2
            mergeSort(arr, low, mid)
            mergeSort(arr, mid+1, high)
            self.merge(arr, low, mid, high)
            return arr
        mergeSort(nums, 0, len(nums)-1)