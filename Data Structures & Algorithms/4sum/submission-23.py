class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        def twoSum(l, r, t):
            temp_ans = []
            while l<=r:
                cs = nums[l] + nums[r]
                if cs > t:
                    r -= 1
                elif cs<t:
                    l += 1
                else:
                    temp_ans.append([nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]: l += 1
                    while l<r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
            return temp_ans
        for i in range(len(nums)):
            # if i>0 and nums[i] == nums[i-1]:
            #     continue
            req_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if j > (i+1) and nums[j] ==nums[j-1]:
                    continue
                req_target -= nums[j]
                req_pairs = twoSum(j+1, len(nums)-1, req_target)
                for pair in req_pairs:
                    pair.append(nums[j])
                    pair.append(nums[i])
                    ans.append(pair)
        return ans
        