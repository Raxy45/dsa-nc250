class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def twoSum( l, r, target: int) -> List[int]:
            # print(target, 'this is', numbers)

            final_nums = []
            while l < r:
                curSum = nums[l] + nums[r]
                # print(curSum, l, r)
                if curSum > target:
                    r -= 1
                elif curSum < target:
                    l += 1
                else:
                    final_nums.append([nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]: l+= 1
                    while l<r and nums[r] == nums[r-1]: r-= 1
                    l += 1
                    r -= 1
            return final_nums

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            req_pair = twoSum(i+1, len(nums)-1, -nums[i])
            for pair in req_pair:
                pair.append(nums[i])
                ans.append(pair)
        print(ans)
        return ans