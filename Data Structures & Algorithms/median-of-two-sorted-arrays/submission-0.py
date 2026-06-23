class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B)<len(B):
            A, B = B, A
        
        total = len(A)+len(B)
        half = total//2
        l, r = 0, len(A)-1

        while True:
            a_mid_i = (l+r)//2
            b_mid_i = half-a_mid_i -2

            A_element_at_left_of_partition  = A[a_mid_i] if a_mid_i>=0 else float('-infinity')
            B_element_at_left_of_partition  = B[b_mid_i] if b_mid_i>=0 else float('-infinity')
            A_element_at_right_of_partition = A[a_mid_i+1] if a_mid_i+1<len(A) else float('infinity')
            B_element_at_right_of_partition = B[b_mid_i+1] if b_mid_i+1<len(B) else float('infinity')
            
            if A_element_at_left_of_partition<=B_element_at_right_of_partition and B_element_at_left_of_partition<=A_element_at_right_of_partition:
                if (total%2)>0:
                    return min(A_element_at_right_of_partition, B_element_at_right_of_partition)
                return (max(A_element_at_left_of_partition, B_element_at_left_of_partition)
                            + min(A_element_at_right_of_partition, B_element_at_right_of_partition))/2

            elif A_element_at_left_of_partition>B_element_at_right_of_partition:
                r = a_mid_i-1
            else:
                l=a_mid_i+1
    