class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []
        heapq.heappush(hp, [-a, 'a']) if a!=0 else None
        heapq.heappush(hp, [-b, 'b']) if b!=0 else None
        heapq.heappush(hp, [-c, 'c']) if c!=0 else None
        ans = ''
        print('initialization hp', hp)
        while hp:
            freq, char = heapq.heappop(hp)
            print('first try', freq, char, hp)
            if ans:
                if len(ans)>1 and char == ans[-1] == ans[-2]:
                    if not hp: return ans
                    freq2, char2 = heapq.heappop(hp)
                    print('second try,', freq2, char2)
                    ans += char2
                    freq2 += 1
                    if freq2 != 0:
                        heapq.heappush(hp, [freq2, char2])
            ans += char
            freq += 1
            if freq != 0:
                heapq.heappush(hp, [freq, char])
            print(ans)
            print(hp)
            print('*'*3)
        return ans      
            


        
