class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        bucket = [[] for i in range(0, len(nums)+1)]
        for num, count in count_map.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            current_bucket = bucket[i]
            for j in current_bucket:
                res.append(j)
                if len(res) == k:
                    return res