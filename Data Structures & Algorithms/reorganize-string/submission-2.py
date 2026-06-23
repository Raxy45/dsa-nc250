class Solution:
    def reorganizeString(self, s: str) -> str:
        count_mp = Counter(s)
        hp = [[-c, char] for char, c in count_mp.items()]
        heapq.heapify(hp)

        ans = ""
        prev = None
        while hp or prev:
            print(hp, prev)
            if not hp:
                if abs(prev[0]) >1:
                    return ""
                    
                ans+=prev[1]
                prev = None
                print('ans', ans)
            else:
                count, char = heapq.heappop(hp)
                ans += char
                count += 1
                if count:
                    if prev:
                        heapq.heappush(hp, prev)
                        prev = None
                    prev = [count, char]
        return ans
