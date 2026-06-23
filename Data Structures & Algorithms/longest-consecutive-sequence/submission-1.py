class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_count = 0
        for i in numSet:
            if (i-1) not in numSet:
                current_count = 0
                while (i+current_count) in numSet:
                    current_count += 1
                max_count = max(max_count, current_count)
        return max_count
















        numSet = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in numSet:
                current_length = 1
                while i + current_length in numSet:
                    current_length += 1
                longest = max(longest, current_length)
        return longest
                