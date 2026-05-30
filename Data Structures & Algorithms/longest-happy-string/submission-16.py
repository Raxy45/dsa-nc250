class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []
        if a:
            heapq.heappush(hp, (-a, 'a'))
        if b:
            heapq.heappush(hp, (-b, 'b'))
        if c:
            heapq.heappush(hp, (-c, 'c'))
        
        ans= ""
        while hp:
            freq, popped = heapq.heappop(hp)
            # print('first', popped, freq)
            # print('current ans', ans)
            if len(ans)>1 and ans[-2] == ans[-1] == popped:
                # print('ans[-2] equals to popped')
                if not hp: return ans
                freq2, popped2 = heapq.heappop(hp)
                # print('second char', popped2, freq2)
                ans += popped2
                freq2 += 1
                if freq2:
                    # print('adding back second char', popped2, freq2)
                    heapq.heappush(hp, (freq2, popped2))
            ans += popped
            freq += 1
            # print('added first char', popped, freq)
            if freq:
                # print('adding back firsty char to hp')
                heapq.heappush(hp, (freq, popped))
            # print('****')
        return ans

