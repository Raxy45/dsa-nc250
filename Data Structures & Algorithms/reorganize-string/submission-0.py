class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        hp = []
        for idx in range(len(s)):
            char = s[idx]
            if not ans or char!=ans[-1]:
                ans.append(char)
                continue
            
            if hp and char!=hp[0][1]:
                ans.append(hp[0][1])
                heapq.heappop(hp)

            heapq.heappush(hp, (idx, char))
            if char == hp[0][1]:
                continue
        
        return "".join(ans)