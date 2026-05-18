class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            if l<r:
                # print('divide', l, r)
                mid = (l+r)//2
                merge(l, mid)
                merge(mid+1, r)
                conquer(l, mid, r)

        def conquer(L, M, R):
            # a, b = nums[L:M+1], nums[M+1:R+1]
            # print('conquering',L, M, R)
            A, B = nums[L:M+1], nums[M+1:R+1]
            indx = L
            i, j = 0, 0
            while i<len(A) and j<len(B):
                if A[i]<B[j]:
                    nums[indx] = A[i]
                    i += 1
                    indx += 1
                else:
                    nums[indx] = B[j]
                    j += 1
                    indx += 1
            
            while i<len(A):
                nums[indx] = A[i]
                i += 1
                indx += 1
            
            while j < len(B):
                nums[indx] = B[j]
                indx += 1
                j += 1
            # print('post conquer', nums)
        merge(0, len(nums)-1)
        return nums