class Solution:
    def merge(self, input_arr, L, M, R):
        left_arr, right_arr = input_arr[L: M+1], input_arr[M+1: R+1]
        input_arr_index, left_index, right_index = L, 0, 0

        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] <= right_arr[right_index]:
                input_arr[input_arr_index] = left_arr[left_index]
                left_index += 1
            else:
                input_arr[input_arr_index] = right_arr[right_index]
                right_index += 1
            input_arr_index += 1
        
        while left_index < len(left_arr):
            input_arr[input_arr_index] = left_arr[left_index]
            left_index +=1
            input_arr_index += 1

        while right_index < len(right_arr):
            input_arr[input_arr_index] = right_arr[right_index]
            right_index +=1
            input_arr_index + 1

    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, l, r):
            if l == r:
                return
            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            self.merge(arr, l, m ,r)
            return arr
        mergeSort(nums, 0, len(nums)-1)
        return nums
        