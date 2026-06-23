class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsS = set(nums)
        count = 0

        for i in nums:
            if i-1 not in numsS:
                # beginning of sequence
                curr_count = 0
                while i+curr_count in numsS:
                    curr_count += 1
                count = max(count, curr_count)
        return count
                