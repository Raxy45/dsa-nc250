class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        m = [float('inf') for _ in range(n)]

        for src2, dest, price in flights:
            graph[src2].append((dest, price))


        q = deque([(0, -1, src)])
        cheapest = float('inf')
        print(graph)
        print(q)
        print('Post initial')
        while q:
            curr_price, stops_req, node = q.popleft()
            print(f'{curr_price = }, {stops_req = }, {node = }')
            if stops_req>k:
                print('stops_req>k')
                continue
            if node == dest:
                print('Dest node popped')
                print(curr_price)
                return curr_price
            
            print('Traversing node', node)
            for dest_stop, price_to_stop in graph[node]:
                print('dest_stop', dest_stop, price_to_stop)
                print('curr dest_stop price', m[dest_stop])
                updated_price = curr_price + price_to_stop
                if m[dest_stop] > updated_price:
                    m[dest_stop] = updated_price
                    q.append((updated_price, stops_req+1, dest_stop))
            
            print(q)
            print('*'*3)
        return -1
