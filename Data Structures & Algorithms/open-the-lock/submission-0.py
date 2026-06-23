class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Start from index 0
        # Find element at index 0
        # proceed with element at index 1
        # repeat

        deadends = set(deadends)
        temp = ['0', '0', '0', '0']
        count = 0
        for i in range(4):
            for j in range(10):
                print(i, j, temp, count)
                temp[i] = str(j)
                if "".join(temp) in deadends:
                    return -1
                if int(target[i]) == j:
                    break
                count += 1
                

        return count

