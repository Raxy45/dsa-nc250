class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_num = sys.maxsize
        n = set(nums)
        for i in nums:
            if i > 0:
                if i < positive_num:
                    print('min', i)
                    positive_num = i
        if positive_num == sys.maxsize:
            return 1
        
        beginning = 0
        current_counter = 1
        while (beginning+current_counter) in n:
            current_counter += 1
        return beginning+current_counter