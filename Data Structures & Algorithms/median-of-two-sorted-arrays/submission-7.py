class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums2)<len(nums1):
            A, B = B, A
        
        total = len(nums1) + len(nums2)
        split = total//2
        low, high = 0, len(A)-1
        while True:
            mid = (low+high)//2
            b_mid = total - mid - 2

            A_left = A[mid] if mid>0 else float('-inf')
            A_right = A[mid+1] if mid<len(A)-1 else float('inf')

            B_left = B[b_mid] if b_mid > 0 else float('-inf')
            B_right = B[b_mid+1] if b_mid<len(B)-1 else float('inf')

            if A_left<=B_right and B_left<=A_right:
                if total%2>0:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right))/2
            elif A_left > B_right:
                high = mid - 1
            else:
                low=mid+1