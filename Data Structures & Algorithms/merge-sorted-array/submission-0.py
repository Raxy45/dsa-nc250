class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1_p, l2_p = m-1,n-1
        ans_p = len(nums1)-1

        while l1_p >= 0 and l2_p >= 0:
            if nums1[l1_p] > nums2[l2_p]:
                nums1[ans_p] = nums1[l1_p]
                l1_p -= 1
            else:
                nums1[ans_p] = nums2[l2_p]
                l2_p -= 1
            ans_p -= 1
        
        print(nums1)
        print(l1_p)
        print(l2_p)
        print(ans_p)
        while l1_p >= 0:
            nums1[ans_p] = nums1[l1_p]
            l1_p -= 1
            ans_p -= 1

        print(nums1)
        print(l1_p)
        print(l2_p)
        print(ans_p)
        while l2_p >= 0:
            nums1[ans_p] = nums2[l2_p]
            l2_p -= 1
            ans_p -= 1
        