class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp, ans = [], ""
        for freq, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if freq:
                heapq.heappush(hp, (freq, char))

        while hp:
            freq, char = heapq.heappop(hp)
            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                # we cant use popped char, we will need to 
                # pop out char from heap again
                if not hp:
                    break
                    # meaning we had only the popped out element present in heap
                    # other than this we dont have any element present, and since it 
                    # is already present more than twice you can return formed string
                    # as ans ex: a=1,b=1,c=7
                
                freq2, char2 = heapq.heappop(hp)
                ans += char2
                freq2 = freq2+1
                if freq2:
                    # if the frequency count is non-zero, only then add it to heap
                    heapq.heappush(hp, (freq2, char2))
            else:
                ans += char
            freq = freq + 1
            if freq:
                heapq.heappush(hp, (freq, char))

        return ans