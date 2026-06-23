class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total_length = len(A) + len(B)
        elem_needed = total_length // 2

        l_A, h_A = 0, len(A) - 1
        while True:
            m_A = (l_A + h_A)//2
            m_B = elem_needed - m_A - 2
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
                h_A = m_A - 1
            else:
                l_A = m_A + 1
            
        

