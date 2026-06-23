class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()  # sort by capital

        max_heap = []
        i = 0
        n = len(projects)

        while k > 0:
            # Push all affordable projects into heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # If no project is affordable, stop
            if not max_heap:
                break

            # Pick the most profitable project
            w += -heapq.heappop(max_heap)
            k -= 1

        return w


    def findMaximizedCapitalMe(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        combined_list = []
        for i in range(len(profits)):
            combined_list.append((capital[i], profits[i]))
        
        combined_list.sort()
        print(combined_list)
        hp = []
        index = 0
        while k > 0:
        
            if index<len(combined_list) and combined_list[index][0] <= w:
                print(combined_list[index][1])
                heapq.heappush(hp, -combined_list[index][1])
                index += 1
                print(hp)
                continue
            
            if hp:
                max_profit = abs(heapq.heappop(hp))
                print('working in project', max_profit)
                print('current w', w)
                print(hp)
                w += max_profit
                k -= 1
            else:
                break
        return w