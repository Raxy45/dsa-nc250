class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L, R, M):
            l_arr, r_arr = nums[L:M+1], nums[M+1:R+1]
            sorted_i = L
            l = r = 0
            while l<len(l_arr) and r<len(r_arr):
                if l_arr[l]<r_arr[r]:
                    nums[sorted_i] = l_arr[l]
                    l += 1
                    sorted_i += 1
                else:
                    nums[sorted_i] = r_arr[r]
                    r += 1
                    sorted_i += 1
                
            while l<len(l_arr):
                nums[sorted_i] = l_arr[l]
                l += 1
                sorted_i += 1
            
            while r<len(r_arr):
                nums[sorted_i] = r_arr[r]
                r += 1
                sorted_i += 1
            
        def mergeSort(l, r):
            if l==r:
                return
            
            mid = (l+r)//2
            mergeSort(l, mid)
            mergeSort(mid+1, r)
            merge(l, r, mid)
        
        mergeSort(0, len(nums)-1)
        return nums
        

        









        def merge(L, R, M):
            arr_l, arr_r = nums[L:M+1], nums[M+1:R+1]
            l_idx, r_idx, sorted_idx = 0, 0, L

            while l_idx<len(arr_l) and r_idx<len(arr_r):
                if arr_l[l_idx]<arr_r[r_idx]:
                    nums[sorted_idx] = arr_l[l_idx]
                    l_idx += 1
                    sorted_idx += 1
                else:
                    nums[sorted_idx] = arr_r[r_idx]
                    r_idx += 1
                    sorted_idx += 1
            
            while l_idx<len(arr_l):
                nums[sorted_idx] = arr_l[l_idx]
                l_idx += 1
                sorted_idx += 1

            while r_idx<len(arr_r):
                nums[sorted_idx] = arr_r[r_idx]
                r_idx += 1
                sorted_idx += 1

        def mergeSort(nums, l ,r):
            if l==r:
                return
            
            mid = (l+r)//2
            mergeSort(nums, l, mid)
            mergeSort(nums, mid+1, r)
            merge(l, r, mid)
        mergeSort(nums, 0, len(nums)-1)
        return nums

        def merge(arr, L, M, R):
            l_a, r_a = arr[L:M+1], arr[M+1:R+1]
            l_i, r_i = 0, 0
            s_i = L

            while l_i < len(l_a) and r_i<len(r_a):
                if l_a[l_i] < r_a[r_i]:
                    arr[s_i] = l_a[l_i]
                    l_i += 1
                else:
                    arr[s_i] = r_a[r_i]
                    r_i += 1
                s_i += 1
            
            while l_i < len(l_a):
                arr[s_i] = l_a[l_i]
                l_i += 1
                s_i += 1

            while r_i<len(r_a):
                arr[s_i] = r_a[r_i]
                r_i += 1
                s_i += 1
        
        def mergeSort(arr, l, r):
            if l == r:
                return
            mid = (l+r)//2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)
            merge(arr, l, mid, r)
            # print('l, mid, r: ', l, mid, r)
            # print('arr: ', arr)
            return arr
        mergeSort(nums, 0, len(nums)-1)
        return nums