class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k_times = len(nums)//3

        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        ans = []
        for key,val in count_map.items():
            if val > k_times:
                ans.append(key)
        return ans