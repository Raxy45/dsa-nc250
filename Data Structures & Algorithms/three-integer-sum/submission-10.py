class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i, target: int) -> List[int]:
            j, k = i+1, len(nums)-1
            ans_pair = []
            while j<k:
                ans = nums[j] + nums[k]
                if ans == target:
                    ans_pair.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while k>j and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                if ans < target:
                    j += 1
                elif ans > target:
                    k -= 1
            print('ans pair', ans_pair )
            return ans_pair
        nums.sort()
        final_ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            required_num = -nums[i]
            current_ans = twoSum(i, required_num)
            if current_ans:
                final_ans.extend(current_ans)
        return final_ans
