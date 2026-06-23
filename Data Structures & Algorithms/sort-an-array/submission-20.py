class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(low, mid, high):
            arr_1, arr_2 = nums[low:mid+1], nums[mid+1:high+1]
            sorted_l = low
            i = j = 0

            while i< len(arr_1) and j<len(arr_2):
                if arr_1[i] < arr_2[j]:
                    nums[sorted_l] = arr_1[i]
                    i += 1
                else:
                    nums[sorted_l] = arr_2[j]
                    j += 1
                sorted_l += 1

            while i<len(arr_1):
                nums[sorted_l] = arr_1[i]
                sorted_l += 1
                i += 1
            
            while j<len(arr_2):
                nums[sorted_l] = arr_2[j]
                sorted_l += 1
                j += 1
            
        def sort(low, high):
            if low<high:
                mid = (low+high)//2
                sort(low, mid)
                sort(mid+1, high)
                mergeSort(low, mid, high)
            
        sort(0, len(nums)-1)
        return nums

