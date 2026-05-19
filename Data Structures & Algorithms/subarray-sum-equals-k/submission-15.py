class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumM = defaultdict(int)
        sumM[0] = 1
        curr_sum = 0
        ans = 0
        for n in nums:
            # print(n)
            curr_sum += n
            required_prefix_sum = curr_sum - k
            # print('required sum', required_prefix_sum)
            if required_prefix_sum in sumM:
                # print('req sum exists in sumM', sumM[required_prefix_sum])
                ans += sumM[required_prefix_sum]
            sumM[curr_sum] += 1
            # print(sumM, ans)
            # print('*****')
        return ans



















        # nums.sort()
        sum_map = defaultdict(int)
        sum_map[0] = 1
        current_sum, ans =0, 0
        for i in nums:
            current_sum += i
            
            required_sum = current_sum - k
            ans += sum_map[required_sum]
            sum_map[current_sum] = sum_map[current_sum] + 1
        return ans