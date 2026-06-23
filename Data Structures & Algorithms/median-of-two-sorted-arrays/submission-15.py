class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B  = nums1, nums2
        if len(B)<len(A):
            A, B = B, A
        
        total_len = len(A)+len(B)
        req_len = total_len //2
        l, r = 0, len(A)-1
        while True:
            mid = (l+r)//2
            mid_b = req_len - mid - 2

            A_elem_lhs = A[mid] if mid>=0  else float('-inf')
            A_elem_rhs = A[mid+1] if (mid+1)<=r else float('inf')

            B_elem_lhs = B[mid_b] if mid_b>=0 else float('-inf')
            B_elem_rhs = B[mid_b+1] if (mid_b+1)<len(B) else float('inf')
            if A_elem_lhs > B_elem_rhs:
                r = mid - 1
            elif A_elem_rhs < B_elem_lhs:
                l = mid + 1
            
            elif A_elem_lhs < B_elem_rhs and B_elem_lhs<A_elem_rhs:
                if (total_len%2) == 0:
                    return (max(A_elem_lhs, B_elem_lhs) + \
                    min(A_elem_rhs, B_elem_rhs))/2
                return min(A_elem_rhs, B_elem_rhs)
