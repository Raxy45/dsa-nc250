class Solution:
    def reorganizeString(self, s: str) -> str:
        s_map = Counter(s)
        hp = []
        for char, count in s_map.items():
            heapq.heappush(hp, [-count, char])
        ans, cooldown = '', []
        idx = 0
        while hp or cooldown:
            print(hp, cooldown, idx)
            if not hp and cooldown:
                return ''
            
            freq, char = heapq.heappop(hp)
            ans += char
            freq += 1
            if cooldown:
                heapq.heappush(hp, cooldown)
            if freq!=0:
                cooldown = [freq, char]
            else:
                cooldown = []
            idx += 1
            if idx == 12:
                break
        return ans