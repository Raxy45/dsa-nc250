class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsS = set(nums)
        count = 0

        for n in nums:
            if n-1 not in numsS:
                # start of sequence
                temp_count = 0 
                while n+temp_count in numsS:
                    temp_count += 1
                count = max(count, temp_count)
        return count
        










        for i in nums:
            if i-1 not in numsS:
                # beginning of sequence
                curr_count = 0
                while i+curr_count in numsS:
                    curr_count += 1
                count = max(count, curr_count)
        return count
                