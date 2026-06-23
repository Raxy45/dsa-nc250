class Solution:
    # def productExceptSelf_basic(self, nums: List[int]) -> List[int]:
    #     total_num_product =  nums[0]
    #     contains_zero = False
    #     zero_count = 0
    #     for i in nums[1:]:
    #         if i!=0:
    #             total_num_product *= i
    #         else:
    #             contains_zero = True
    #             zero_count += 1
    #     print(total_num_product)

    #     ans = []
    #     for i in nums:
    #         current_ans = total_num_product
    #         if i!=0:
    #             current_ans = int(total_num_product/i)
    #             if contains_zero:
    #                 current_ans = 0
    #         if zero_count > 1:
    #             current_ans = 0
    #         ans.append(current_ans)
    #     return ans

        # def productExceptSelf(self, nums: List[int]) -> List[int]:
        #     current_m = nums[0]
        #     left_m = [current_m]
        #     for i in nums[1:]:
        #         current_m = i*current_m
        #         left_m.append(current_m)
            
        #     right_m = [1]*len(nums)
        #     current_m = nums[-1]
        #     right_m[-1] = current_m
        #     for i in range(len(nums)-2, -1, -1):
        #         current_m = current_m*nums[i]
        #         print(i)
        #         right_m[i] = current_m
            
        #     i = 0
        #     while i<len(nums):
        #         if i == 0:
        #             nums[i] = right_m[i+1]
        #         elif i == len(nums) -1:
        #             nums[i] = left_m[i-1]
        #         else:
        #             nums[i] = left_m[i-1]*right_m[i+1]
        #         i+=1
        #     return nums

        # def productExceptSelf(self, nums: List[int]) -> List[int]:
        #     current_m = nums[0]
        #     ans = [current_m]
        #     for i in nums[1:]:
        #         current_m = i*current_m
        #         ans.append(current_m)
            
        #     print(ans)
        #     right_m = nums[len(nums)-1]
        #     ans[len(nums)-1] = ans[len(nums)-2]

        #     print(ans)
        #     for i in range(len(nums)-2,-1,-1):
        #         print(i, right_m)
        #         if i == 0:
        #             ans[i] = right_m
        #         else:
        #             ans[i] = right_m*ans[i-1]
        #         right_m = right_m*nums[i]
        #     return ans

        def productExceptSelf(self, nums: List[int]) -> List[int]:
            prefix = 1
            ans = [1]*len(nums)
            for i in range(len(nums)):
                ans[i] = prefix
                prefix = prefix*nums[i]
            print(ans)

            postfix = 1
            for i in range(len(nums)-1, -1, -1):
                print(i, postfix, ans[i])
                print('*'*30)
                ans[i] = postfix*ans[i]
                postfix = postfix*nums[i]
            return ans

