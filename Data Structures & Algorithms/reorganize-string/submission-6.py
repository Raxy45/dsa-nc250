class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        hp = [(-c, char) for char, c in Counter(s).items()]
        heapq.heapify(hp)
        prev = None
        counter = 0
        while prev or hp:
            if prev and not hp:
                return ""
            if hp:
                freq, popped = heapq.heappop(hp)
                freq += 1
                ans += popped
                if prev: 
                    heapq.heappush(hp, prev)
                    prev = None
                if freq:
                    prev = (freq, popped)
            counter += 1
        return ans
        