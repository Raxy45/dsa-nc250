class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, h = 0, len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m]==t: return m

            if nums[l]<=nums[m]:
                if nums[l]<=t<=nums[m]: r=m-1
                else: l=m+1
            else:
                if nums[m]<=t<=nums[r]: l = m+1
                else: r=m-1
        return -1