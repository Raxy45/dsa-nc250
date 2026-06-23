class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, num in enumerate(nums):
            required_num = target - nums[i]
            if required_num in my_map:
                return [my_map[required_num], i]
            my_map[num] = i
        return []