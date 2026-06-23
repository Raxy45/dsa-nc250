class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, num in enumerate(my_map):
            required_num = target - nums[i]
            if required_num in my_map:
                return [i, nums.index(required_num)]
            my_map[num] = i
        return []