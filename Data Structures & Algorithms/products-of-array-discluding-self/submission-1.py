class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_num_product =  nums[0]
        contains_zero = False
        for i in nums[1:]:
            if i!=0:
                total_num_product *= i
            else:
                contains_zero = True
        print(total_num_product)

        ans = []
        for i in nums:
            current_ans = total_num_product
            if i!=0:
                current_ans = int(total_num_product/i)
                if contains_zero:
                    current_ans = 0
            ans.append(current_ans)
        return ans

        