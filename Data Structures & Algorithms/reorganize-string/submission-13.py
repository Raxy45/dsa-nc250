class Solution:
    def reorganizeString(self, s: str) -> str:
        char_mp = Counter(s)
        hp = []
        for k, v in char_mp.items():
            hp.append((-v, k))
        heapq.heapify(hp)
        prev = None

        ans = ""
        j = 0
        while hp:            
            freq, curr = heapq.heappop(hp)
            ans += curr
            freq += 1

            if prev: 
                heapq.heappush(hp, prev)
            
            if freq:
                prev = (freq, curr)
            else:
                prev = None
            
            # j += 1
        
        if prev:
            return ""
        return ans