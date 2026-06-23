class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count_map = {}
        # for i in nums:
        #     count_map[i] = count_map.get(i, 0) + 1
        
        # size = len(nums) // 2
        # for i in count_map:
        #     if count_map[i] > size:
        #         return i
        # nums.sort()
        # i = 0
        # if len(nums) == 1:
        #     return nums[0]
        # while i < len(nums) - 1:
        #     k = 1
        #     current_element = -1
        #     while i < len(nums) -1 and nums[i + 1] == nums[i]:
        #         current_element = nums[i]
        #         k += 1
        #         i += 1
        #     if k > len(nums) // 2:
        #         return current_element
        #     i += 1
        i = res = count = 0
        while i<len(nums):
            if i == 0:
                res=nums[i]
            if count == 0:
                res = nums[i]
            if nums[i] == res:
                count += 1
            else:
                count -= 1
            i += 1
        return res





        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            print(count, res, num)
            count += (1 if num == res else -1)
        return res
        