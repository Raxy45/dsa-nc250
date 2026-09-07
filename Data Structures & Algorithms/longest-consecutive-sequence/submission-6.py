class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        ans = 1
        for n in nums:
            i = n
            count = 0
            if (i-1) not in ns:
                while i in ns:
                    count += 1
                    ans = max(ans, count)
                    i += 1
        return ans
        