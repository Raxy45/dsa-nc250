class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in numSet:
                print(i)
                current_length = 0
                while i + current_length in numSet:
                    current_length += 1
                longest = max(longest, current_length)
        return longest
                