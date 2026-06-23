class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        count = 0
        prefix_sum = 0
        print(prefix_map, type(prefix_map))
        for i in nums:
            prefix_sum = prefix_sum + i
            old_prefix_sum_we_can_chio_off = prefix_sum - k
            if old_prefix_sum_we_can_chio_off in prefix_map:
                count += prefix_map[old_prefix_sum_we_can_chio_off]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

            # print('i', i)
            # print('prefix_sum', prefix_sum)
            # print('old_prefix_sum_we_can_chio_off', old_prefix_sum_we_can_chio_off)
            # print('prefix_map', prefix_map)
            # print('count', count)
        return count        