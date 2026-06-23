class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        print(count_map)
        sorted_freq_count = sorted(list(count_map.values()))
        print(f'{sorted_freq_count = }')
        print(type(sorted_freq_count))
        
        # print(f'{K_freq_count = }')
        ans = []
        i = len(sorted_freq_count) - 1
        print(sorted_freq_count)
        while(k>0):
            ans.append(sorted_freq_count[i])
            i -= 1
            k -= 1
        
        a = []
        for i in count_map:
            if count_map[i] in ans:
                a.append(i)

        return a