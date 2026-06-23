class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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