class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        combined_list = []
        for i in range(len(profits)):
            combined_list.append((capital[i], profits[i]))
        
        combined_list.sort()
        print(combined_list)
        hp = []
        index = 0
        while k > 0 and index<=len(combined_list):
        
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
                index += 1
        return w