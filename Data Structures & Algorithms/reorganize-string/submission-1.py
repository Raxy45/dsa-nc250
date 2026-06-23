class Solution:
    def reorganizeString(self, s: str) -> str:
        char_map = Counter(s)
        hp = []
        for char, freq in char_map.items():
            heapq.heappush(hp, (-freq, char))
        
        prev, ans = None, ""
        while hp or prev:
            if prev and not hp:
                # meaning we have empty heap, but there exists some element
                # which cant be used in the ans, example a:3, b:1
                return ""
            freq, char = heapq.heappop(hp)
            ans+=char
            freq += 1

            if prev:
                heapq.heappush(hp, (prev[0], prev[1]))
                prev = None
            if freq:
                prev = [freq, char]
        return ans