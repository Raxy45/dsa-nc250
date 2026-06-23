class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        positive_arr = []
        max_int = -sys.maxsize-1
        for i in nums:
            if i > 0:
                positive_arr.append(i)
            if i > max_int:
                max_int = i
        if len(positive_arr) == 0:
            return 1
        
        arr = [0]*(max_int+1)
        for i in positive_arr:
            arr[i] = 1
        print(arr)

        for i in range(1, len(arr)):
            if arr[i] == 0:
                return i



        positive_num = sys.maxsize
        n = set(nums)
        for i in nums:
            if i > 0:
                if i < positive_num:
                    print('min', i)
                    positive_num = i
        if positive_num == sys.maxsize:
            return 1
        
        beginning = 0
        current_counter = 1
        while (beginning+current_counter) in n:
            current_counter += 1
        return beginning+current_counter