class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        hp = [(-c, char) for char, c in Counter(s).items()]
        heapq.heapify(hp)
        prev = None
        counter = 0
        while prev or hp:
            if counter > 10: break
            if prev and not hp:
                return ""
            print(hp)
            print('ans', ans)
            print('prev', prev)
            if hp:
                freq, popped = heapq.heappop(hp)
                freq += 1
                ans += popped
                print('popped', popped)
                print('freq', freq)
                if prev: 
                    print('adding prev to hp', prev)
                    heapq.heappush(hp, prev)
                    prev = None
                if freq:
                    print('updating freq')
                    prev = (freq, popped)
                    print('prev set to', prev)
            print('updated ans', ans)
            counter += 1
            print('*'*5)
        return ans
        