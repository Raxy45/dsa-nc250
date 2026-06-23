class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums_s, k):
            l = 0
            r = len(nums_s)-1
            ans = []
            while l<r:
                current_sum = nums_s[l]+nums_s[r]
                print('nums_sss[l], nums_SSS[r]', nums_s[l], nums_s[r])
                print('current sum', current_sum)
                # print('l, r, k', l, r, k)
                if current_sum==k:
                    print('current_sum==k')
                    ans.append([nums_s[l], nums_s[r]])
                    print(ans)
                    while l<r and nums_s[l]==nums_s[l+1]:
                        l = l+1
                    l += 1

                    while l<r and nums_s[r] == nums_s[r-1]:
                        r = r-1
                    r = r-1

                    # print('final l and r after dupe skipping', nums_s[l], nums_s[r])
                elif current_sum > k:
                    r = r-1
                else:
                    l = l+1
            return ans
        nums.sort()
        print(nums)
        l = 0
        r = len(nums) -1
        diff = r - l
        final_ans = []
        do_left = False
        while diff > 2:
            updated_arr = nums[l+1: r]
            print(updated_arr)
            print('nums[l], nums[r]', nums[l], nums[r])
            current_target = target - (nums[l]+nums[r])
            print('cirremt target: ', current_target)
            ans = twoSum(updated_arr, current_target)
            
            print('ans for nums[l], nums[r]', nums[l], nums[r])
            print(ans)
            if len(ans)>0:
                for i in ans:
                    print(i)
                    final_ans.append([nums[l], nums[r], i[0], i[1]])
            
            print(final_ans)
            diff = r - l
            while (r-l)>2 and nums[l] == nums[l+1]:
                l += 1

            while (r-l)>2 and nums[r] == nums[r-1]:
                r -= 1
            
            if do_left is True:
                l = l+1
                do_left = False
            else:
                r= r-1
                do_left=True
            diff = r - l
        return final_ans
        
