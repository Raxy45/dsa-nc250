class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, curr = 0, nums[0]
        for n in nums:
            if curr == n:
                count += 1
                continue
            
            if curr != n:
                count -= 1
            
            if count == 0:
                curr = n
                count += 1
        return curr







        count = 0
        for i in nums:
            if count == 0:
                ans = i

            if i == ans:
                count += 1
            else:
                count -= 1
        return ans