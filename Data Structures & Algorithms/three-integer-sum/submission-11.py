class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def twoSum(i, target: int) -> List[int]:
            j, k = i+1, len(nums)-1
            c_sum = 0
            while j<k:
                c_sum = nums[j] + nums[k]
                if c_sum == target:
                    ans.append([nums[i], nums[j], nums[k]])

                    # below while loop
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while k>j and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                if c_sum < target:
                    j += 1
                elif c_sum > target:
                    k -= 1
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            required_num = -nums[i]
            twoSum(i, required_num)
        return ans
