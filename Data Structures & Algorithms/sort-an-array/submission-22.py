class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, mid, r):
            # print(f'{nums = }')
            # print('merging for', l, mid, r)
            arr_1, arr_2 = nums[l:mid+1], nums[mid+1:r+1]
            start, i, j = l, 0, 0
            # print(f'{arr_1 = }', f'{arr_2 = }')
            while i<len(arr_1) and j<len(arr_2):
                if arr_1[i] < arr_2[j]:
                    # print('i less than j')
                    nums[start] = arr_1[i]
                    i += 1
                else:
                    # print('j less than i')
                    nums[start] = arr_2[j]
                    j += 1
                # print(nums)
                start += 1
            
            # print('post nums', nums)
            # print(start, i, 'after both')
            while i<len(arr_1):
                nums[start] = arr_1[i]
                start += 1
                i += 1

            while j<len(arr_2):
                nums[start] = arr_2[j]
                start += 1
                j += 1

        def Sort(i, j):
            if i<j:
                # print(i, j)
                mid = (i+j)//2
                Sort(i, mid)
                Sort(mid+1, j)
                merge(i, mid, j)

        Sort(0, len(nums)-1)
        return nums
