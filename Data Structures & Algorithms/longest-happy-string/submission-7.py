class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(hp)
        ans = ""
        while hp:
            print('b4 hp', hp)
            freq1, popped1 = heapq.heappop(hp)
            if len(ans)>1 and ans[-1] == ans[-2] == popped1:
                if not hp: return ans
                freq2, popped2 = heapq.heappop(hp)
                if freq2:
                    ans += popped2
                    freq2 += 1
                    if freq2:
                        heapq.heappush(hp, (freq2, popped2))
            else:
                if freq1:
                    ans+= popped1
                    freq1 += 1
            if freq1:
                heapq.heappush(hp, (freq1, popped1))
            print('after hp', hp)
            print(ans)
            print('*'*10)
        return ans