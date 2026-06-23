class Solution:
    def canonical_triplet_set(self, triplet):
    # sort the elements and return as a tuple (hashable)
        return tuple(sorted(triplet))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        a = []
        # def twoSum(l, r, required_sum):
        #     print(required_sum, l, r)
        #     current_ans = []
        #     while l<r:
        #         curr_sum = sorted_nums[l]+sorted_nums[r]
        #         if curr_sum==required_sum:
        #             current_ans.append((sorted_nums[l], sorted_nums[r]))
        #             while l<r and sorted_nums[l]==sorted_nums[l+1]:
        #                 l += 1
        #             while l<r and sorted_nums[r]==sorted_nums[r-1]:
        #                 r -= 1
        #         elif curr_sum<required_sum:
        #             l += 1
        #         else:
        #             r -= 1
        #     print(current_ans, l, r)
        #     return current_ans
        
        # for i in range(len(nums)-2):
        #     req_sum = -sorted_nums[i]
        #     if i>0 and sorted_nums[i] == sorted_nums[i-1]:
        #         continue
        #     req_pair = twoSum(i+1,len(sorted_nums)-1, req_sum)
        #     if len(req_pair) > 0:
        #         for curr_ans in req_pair:
        #             ans.append((sorted_nums[i], curr_ans[0], curr_ans[1]))
        # return ans














        def twoSum(l,r, current_index):
            target = -sorted_nums[current_index]
            print('target', target)
            while l < r:
                c_sum = sorted_nums[l]+sorted_nums[r]
                if c_sum==target:
                    a.append([sorted_nums[current_index], sorted_nums[l], sorted_nums[r]])
                    # skip duplicates before moving pointers
                    while l < r and sorted_nums[l] == sorted_nums[l+1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif c_sum > target:
                    r -= 1
                else:
                    l += 1
        print('sorted nums', sorted_nums)
        for i in range(0, len(nums)-2):
            if i>0 and sorted_nums[i]==sorted_nums[i-1]:
                print(i, 'skipped')
                continue
            twoSum(i+1, len(sorted_nums)-1, i)
        print(a)
        return a
                    