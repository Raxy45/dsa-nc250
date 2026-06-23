class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        combined_arr = list(zip(capital, profits))
        combined_arr.sort()
        combined_arr = deque(combined_arr)
        hp = []
        task = None
        while True:
            print(combined_arr)
            while combined_arr and w>=combined_arr[0][0]:
                popped_proj = combined_arr.popleft()
                heapq.heappush(hp, (-popped_proj[1]))
            
            print(hp)
            if not hp or k==0:
                return w
            w += -(heapq.heappop(hp))
            k -= 1
            print(w)
            print('*'*5)