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
            print('popped', freq, curr)
            ans += curr
            freq += 1

            if prev: 
                print('prev existed, added to hp', prev)
                heapq.heappush(hp, prev)
            
            if freq:
                print('popped out char has freq>0, setting it to prev')
                prev = (freq, curr)
            else:
                prev = None
            
            # j += 1
        
        if prev:
            return ""
            remaining = prev[0]
            print('remaining count is', remaining, 'of', prev[1])
            while remaining:
                ans += curr
                remaining += 1
        return ans