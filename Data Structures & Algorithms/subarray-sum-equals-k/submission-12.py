class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_map = defaultdict(int)
        sum_map[0] = 1
        current_sum, ans =0, 0
        for i in nums:
            current_sum += i
            
            required_sum = current_sum - k
            ans += sum_map[required_sum]
            sum_map[current_sum] = sum_map[current_sum] + 1
        return ans