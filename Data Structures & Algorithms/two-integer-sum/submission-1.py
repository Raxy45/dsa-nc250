class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, key in enumerate(nums):
            my_map[key] = i

        print(my_map)
        for i, num in enumerate(nums):
            required_num = target - nums[i]
            required_num_index = my_map.get(required_num, -1)
            print(required_num, required_num_index)
            if required_num_index != -1 and required_num_index!=i:
                return [i, required_num_index]