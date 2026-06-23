class Solution:
    def split(self, arr):
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]
        return left_arr, right_arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        left_arr, right_arr = self.split(nums)
        left_sorted = self.sortArray(left_arr)
        right_sorted = self.sortArray(right_arr)
        return self.merge(left_sorted, right_sorted)
        
    def merge(self, left_arr, right_arr):
        sorted_arr = []
        right_index = left_index = 0
        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                sorted_arr.append(left_arr[left_index])
                left_index += 1
            else:
                sorted_arr.append(right_arr[right_index])
                right_index += 1
        if left_index < len(left_arr):
            sorted_arr.extend(left_arr[left_index:])
        if right_index < len(right_arr):
            sorted_arr.extend(right_arr[right_index:])
        return sorted_arr