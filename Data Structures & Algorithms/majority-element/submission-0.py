class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        size = len(nums) // 2
        for i in count_map:
            if count_map[i] > size:
                return i
        