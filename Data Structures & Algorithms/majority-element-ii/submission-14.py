from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res
        
    def majorityElementEz(self, nums: List[int]) -> List[int]:
        k_times = len(nums)//3

        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        ans = []
        for key,val in count_map.items():
            if val > k_times:
                ans.append(key)
        return ans