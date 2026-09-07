class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        ans = nums[0]
        for n in nums:
            if counter == 0:
                ans = n

            if n ==ans:
                counter += 1
            else:
                counter -= 1
        return ans
        