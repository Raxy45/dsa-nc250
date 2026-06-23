class Solution:
    def calPoints(self, operations: List[str]) -> int:
        updated_arr = []
        i = 0
        j = 0
        while i<len(operations):
            current_char = operations[i]
            if current_char == '+':
                print('i, ', i)
                updated_arr.append(int(updated_arr[j-1]) + int(updated_arr[j-2]))
                j += 1
                i += 1
            elif current_char == 'D':
                updated_arr.append(2*int(updated_arr[j-1]))
                j += 1
                i += 1
            elif current_char == 'C':
                updated_arr.pop()
                j -= 1
                i += 1
            else:
                updated_arr.append(int(operations[i]))
                j += 1
                i += 1
        print(updated_arr)
        final_ans = 0
        for x in updated_arr:
            final_ans += x
        return final_ans