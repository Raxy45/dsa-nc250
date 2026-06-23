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

        for i in range(len(nums)):
            if i>0:
                if nums[i] == nums[i-1]:
                    continue
            print('i', i, nums[i])
            for j in range(i + 1, len(nums)):
                print('j before', j, ' i ', i)
                if j!=(i+1): # we've something like [1,1,2,3,4]  We skip this because when j
                #  is i +1, the value j-1 will be equal to i and we are not going to
                #  consider it in the first place, as it is before the range
                    if nums[j] == nums[j-1]:
                        continue
                print('j', j, nums[j])
                two_sum_target = target - nums[i] - nums[j]
                print('two sum target', two_sum_target)
                ans = twoSum(nums[j + 1:], two_sum_target)
                for pair in ans:
                    print('ans found', ans)
                    final_ans.append([nums[i], nums[j]] + pair)
                    print('final ans', final_ans)
                print('#'*10)
            print('*'*30)
        # do_left = False
        # while diff > 2:
        #     updated_arr = nums[l+1: r]
        #     print(updated_arr)
        #     print('nums[l], nums[r]', nums[l], nums[r])
        #     current_target = target - (nums[l]+nums[r])
        #     print('cirremt target: ', current_target)
        #     ans = twoSum(updated_arr, current_target)
            
        #     print('ans for nums[l], nums[r]', nums[l], nums[r])
        #     print(ans)
        #     if len(ans)>0:
        #         for i in ans:
        #             print(i)
        #             final_ans.append([nums[l]] + i + [nums[r]])
            
        #     print(final_ans)
        #     diff = r - l
        #     while (r-l)>2 and nums[l] == nums[l+1]:
        #         l += 1

        #     while (r-l)>2 and nums[r] == nums[r-1]:
        #         r -= 1
            
        #     if do_left is True:
        #         l = l+1
        #         do_left = False
        #     else:
        #         r= r-1
        #         do_left=True
        #     diff = r - l
        return final_ans
        
