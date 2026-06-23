class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Find total elements -> number of elements required to get median = total//2
        # 2. Do Binary search on min length array -> mid_A -> ending point from A
        # 3. mid_B = total//2 - mid_A - 2
        # 4. Compare A_left w B_right and vice versa
        # 5. if A_left > B_right -> decrease size of ans array in A -> h_A - m_A

        A, B = nums1, nums2
        if len(B) < len(A):
            # we want to do Binary Search on A, therefore better to have 
            # lower number of elements in Binary Searched Array
            A, B = B, A
        
        total_length = len(A) + len(B)
        
        elems_needed = total_length // 2
        l_A, h_A = 0, len(A) - 1
        while True:
            # middle of A and middle of B, represents the ending points of two answer arrays
            m_A = (l_A+h_A) // 2

            m_B = elems_needed - m_A - 2

            A_left = A[m_A] if m_A>=0 else float('-inf')
            A_right = A[m_A+1] if (m_A+1) < len(A) else float('inf')
            B_left = B[m_B] if m_B>=0 else float('-inf')
            B_right = B[m_B+1] if (m_B+1) < len(B) else float('inf')

            if A_left<=B_right and B_left<=A_right:
                if total_length%2>0:
                    return min(A_right, B_right)
                else:
                    print('in here')
                    return ((max(A_left, B_left) + min(A_right, B_right)))/2
            if A_left > B_right:
                # We need to decrease elements from A
                h_A = m_A - 1
            else:
                l_A = m_A + 1
        
        

