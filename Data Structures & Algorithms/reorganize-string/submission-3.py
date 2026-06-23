class Solution:
    def reorganizeString(self, s: str) -> str:
        hp = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(hp)

        ans, prev = "", None
        while hp or prev:
            if prev and not hp: return ""

            freq, char = heapq.heappop(hp)
            ans += char
            freq += 1

            if prev:
                heapq.heappush(hp, prev)
                prev = None
            
            if freq:
                prev = (freq, char)
        return ans